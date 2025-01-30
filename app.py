from flask import Flask, render_template, request, jsonify, send_file, session
import re
from collections import defaultdict
import csv
import io
import json
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

def parse_snyk_report(content):
    # Split the content into lines
    lines = content.split('\n')
    
    # Initialize variables
    issues = []
    current_issue = None
    
    for line in lines:
        # Match issue header
        issue_match = re.match(r'\s*[✗]\s+\[(.*?)\]\s+(.*?)$', line)
        if issue_match:
            if current_issue:
                issues.append(current_issue)
            severity = issue_match.group(1)
            title = issue_match.group(2)
            current_issue = {
                'severity': severity,
                'title': title,
                'path': '',
                'info': ''
            }
            continue

        # Match path
        path_match = re.match(r'\s*Path:\s+(.*?)(?:,\s+line\s+(\d+))?$', line)
        if path_match and current_issue:
            current_issue['path'] = path_match.group(1)
            current_issue['line'] = path_match.group(2)
            continue

        # Match info
        info_match = re.match(r'\s*Info:\s+(.*?)$', line)
        if info_match and current_issue:
            current_issue['info'] = info_match.group(1)
            continue

    # Add the last issue
    if current_issue:
        issues.append(current_issue)

    # Group similar issues
    grouped_issues = defaultdict(list)
    for issue in issues:
        # Group by severity, title and info (since these would be same for similar issues)
        key = (issue['severity'], issue['title'], issue['info'])
        grouped_issues[key].append(issue)

    # Convert to list of grouped issues
    final_issues = []
    for (severity, title, info), instances in grouped_issues.items():
        final_issues.append({
            'severity': severity,
            'title': title,
            'info': info,
            'instances': instances,
            'count': len(instances)
        })

    # Count severities
    summary = {
        'High': len([i for i in issues if i['severity'] == 'High']),
        'Medium': len([i for i in issues if i['severity'] == 'Medium']),
        'Low': len([i for i in issues if i['severity'] == 'Low'])
    }

    return {
        'issues': final_issues,
        'summary': summary
    }

@app.route('/export/<format>')
def export_report(format):
    # Get the report data from session or regenerate it
    report_data = session.get('report_data', {})
    
    if format == 'json':
        return jsonify(report_data)
    
    elif format == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Severity', 'Title', 'Info', 'Path', 'Line'])
        
        for issue in report_data['issues']:
            for instance in issue['instances']:
                writer.writerow([
                    issue['severity'],
                    issue['title'],
                    issue['info'],
                    instance['path'],
                    instance.get('line', '')
                ])
        
        output.seek(0)
        return output.getvalue()
    
    elif format == 'pdf':
        pdf = FPDF()
        pdf.add_page()
        
        # Add title
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Snyk Security Report', 0, 1, 'C')
        
        # Add summary
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Summary', 0, 1)
        pdf.set_font('Arial', '', 12)
        for severity, count in report_data['summary'].items():
            pdf.cell(0, 10, f'{severity}: {count}', 0, 1)
        
        # Add issues
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Vulnerabilities', 0, 1)
        
        for issue in report_data['issues']:
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, f"{issue['severity']}: {issue['title']}", 0, 1)
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(0, 10, f"Info: {issue['info']}")
            
            for instance in issue['instances']:
                pdf.multi_cell(0, 10, f"Path: {instance['path']}")
                if instance.get('line'):
                    pdf.cell(0, 10, f"Line: {instance['line']}", 0, 1)
            
            pdf.cell(0, 5, '', 0, 1)  # Add some spacing
        
        return send_file(
            io.BytesIO(pdf.output(dest='S').encode('latin-1')),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='snyk-report.pdf'
        )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400

        content = file.read().decode('utf-8')
        report_data = parse_snyk_report(content)
        session['report_data'] = report_data  # Store in session
        return render_template('report.html', report=report_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 