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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Snyk for providing the vulnerability scanning capabilities
- Flask framework for the web application
- All contributors who participate in this project
