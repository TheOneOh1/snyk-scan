# Snyk Vulnerability Report Dashboard

A web-based dashboard for visualizing and managing Snyk vulnerability reports. This tool provides a clean, interactive interface to view and analyze security vulnerabilities detected by Snyk.

## Features

- **Interactive Dashboard**: Clean and intuitive interface for viewing vulnerability reports
- **Vulnerability Grouping**: Similar vulnerabilities are grouped together for better organization
- **Severity-based Classification**: Vulnerabilities are categorized by High, Medium, and Low risk levels
- **Quick Navigation**: Click on severity counts to jump to corresponding vulnerabilities
- **Export Options**: Export reports in multiple formats (PDF, CSV, JSON)
- **Drag & Drop**: Easy file upload with drag and drop functionality
- **Copy to Clipboard**: Quick copying of vulnerability details
- **Expandable Details**: Click to view detailed information about each vulnerability
- **Dark Theme**: Easy on the eyes with a modern dark theme

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/snyk-dashboard.git
cd snyk-dashboard
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Export your Snyk vulnerability report as a text file
2. Drag and drop the file onto the dashboard or use the file picker
3. View the organized vulnerability report with interactive features
4. Export the report in your preferred format (PDF, CSV, JSON)
5. Click on severity counts to navigate to specific vulnerabilities
6. Use the copy button to copy vulnerability details to clipboard

## Future Scope

### Report Management
- Track reports with unique IDs using project paths as reference
- Maintain scan history for each project
- Compare reports to track vulnerability trends
- Show graphs/charts of vulnerability trends over time
- Add notes/comments to specific vulnerabilities

### Enhanced Filtering & Search
- Filter vulnerabilities by file path, severity, or type
- Search functionality for finding specific vulnerabilities
- Sort vulnerabilities by different criteria
- Tag system for better organization
- Filter by new/existing/resolved vulnerabilities

### User Experience Improvements
- Keyboard shortcuts for navigation
- Collapsible sidebar for better navigation
- Toast notifications for actions
- Custom dashboard layouts
- Branding options

### Integration & Authentication
- Integration with GitHub/GitLab for direct repository scanning
- User authentication system
- Team collaboration features
- Share reports via unique URLs
- API endpoints for programmatic access
- Integration with CI/CD pipelines

### Vulnerability Management
- Mark vulnerabilities as "in progress", "ignored", or "resolved"
- Set priority levels for vulnerabilities
- Assign vulnerabilities to team members
- Add custom labels/tags
- Set reminders for follow-up actions

### Enhanced Visualization
- Heat maps showing vulnerability concentrations
- Tree view of affected files/directories
- Timeline view of when vulnerabilities were introduced
- Dependency graphs showing affected components
- Custom dashboard widgets

### Documentation & Help
- Tooltips explaining vulnerability types
- Links to vulnerability databases (CVE, CWE)
- Suggested fixes for common vulnerabilities
- Best practices documentation
- Interactive tutorial for new users

### Performance & Technical
- Implement caching for better performance
- Support for larger report files
- Batch processing of multiple reports
- Real-time updates using WebSocket
- Progressive loading for large reports

### Notification System
- Email alerts for new high-severity vulnerabilities
- Slack/Teams integration for notifications
- Custom notification rules
- Weekly/monthly summary reports
- Alert thresholds configuration

### Compliance & Reporting
- Compliance status tracking
- Custom report templates
- Automated report generation
- Audit logs of all actions
- GDPR/HIPAA compliance features

### Mobile Support
- Native mobile app
- Push notifications
- Mobile-optimized views
- Offline support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Snyk for providing the vulnerability scanning capabilities
- Flask framework for the web application
- All contributors who participate in this project

2. Create a virtual environment (recommended):