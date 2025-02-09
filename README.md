# MSME-Bank-Statement-Analyzer-for-Loan-Underwriting
A powerful Flask-based web application that analyzes bank statements to facilitate loan underwriting decisions. This tool provides comprehensive financial insights through interactive visualizations and detailed PDF reports.
App Demo :

File Upload:
![image](https://github.com/user-attachments/assets/73b403d0-8bf5-47e0-ac56-1603f50392dd)

In-Depth Analysis (After Clicking 'Analyze Statement')
![image](https://github.com/user-attachments/assets/6637db38-a276-4ac6-bc58-0def12fd0acc)
![image](https://github.com/user-attachments/assets/c5a68b23-2fcd-4334-b68b-b40f613dcd59)
![image](https://github.com/user-attachments/assets/dc0577de-545d-41bf-aa36-40059830ee01)

Downloadable PDF Report (After Clicking 'Download Full PDF')
![image](https://github.com/user-attachments/assets/7556bb1d-fece-488b-a4b1-8e1aa29bcf85)
![image](https://github.com/user-attachments/assets/a0964b0f-e764-4da0-b837-f2805f064ade)
![image](https://github.com/user-attachments/assets/6fca2eb1-caf5-48a8-b411-faa7837b78e7)

🌟 Features
Core Analysis
Transaction pattern analysis
Monthly credit & debit comparison
Balance trend visualization
Risk assessment indicators
PDF report generation
Financial Metrics
Total credits & debits
Monthly cash flow insights
Average & highest/lowest transactions
Balance fluctuation patterns
Risk Assessment
Negative balance tracking
Zero transaction days monitoring
Monthly spending trends
Income stability indicators
Visualization
Interactive charts & graphs
Transaction type distribution
Color-coded insights
Fully responsive design
🛠️ Tech Stack
Backend: Python Flask
Frontend: HTML, TailwindCSS, Font Awesome
Data Processing: Pandas
Visualization: Matplotlib
PDF Generation: FPDF
📋 Prerequisites
Python 3.8+
pip (Python package manager)
Modern web browser
Basic command-line knowledge



🚀 Installation

1. Clone the repository: 
   git clone https://github.com/yourusername/bank-statement-analyzer.git
   cd bank-statement-analyzer

2. Create a virtual environment (recommended):
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt
   
4. Run the application:
   python app.py

Project Schema :
bank-statement-analyzer/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── static/
│   └── images/           # Generated charts and images
├── templates/
│   ├── index.html        # Upload interface
│   └── report.html       # Analysis dashboard
├── uploads/              # Temporary storage for uploads
└── reports/              # Generated PDF reports

💡 Use Cases

Loan Officers

Quick assessment of borrower's financial health
Standardized analysis across applications
Risk factor identification
Documentation for loan files


Financial Advisors

Client financial behavior analysis
Income pattern recognition
Spending habit assessment
Professional report generation


Credit Analysts

Credit worthiness evaluation
Cash flow analysis
Transaction pattern study
Risk assessment


Small Business Lenders

Business cash flow analysis
Seasonality identification
Working capital assessment
Revenue pattern analysis



🔒 Security Features

Secure file upload handling
Temporary file storage with automatic cleanup
No permanent data storage
Client-side file validation
Server-side file type verification

🔄 Process Flow

User uploads bank statement
System validates file format
Data processing and analysis
Generation of interactive visualizations
Creation of comprehensive PDF report
Display of analysis dashboard
Option to download detailed report

🚀 Future Improvements

Enhanced Analysis

Machine learning for pattern recognition
Anomaly detection
Fraud indicators
Industry-specific analysis


Additional Features

Multiple statement comparison
Custom date range analysis
Category-wise spending analysis
Recurring payment detection


User Experience

Dark mode support
Multiple language support
Mobile app version
Custom report templates


Integration Capabilities

API endpoints for third-party integration
Direct bank feed support
Export to various formats
Cloud storage integration

🙏 Acknowledgments

Flask Documentation
Pandas Documentation
Matplotlib Documentation
TailwindCSS Community
Font Awesome Icons





