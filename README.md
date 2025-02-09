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

**# Bank Statement Analyzer**

## 🌟 Features

### **Core Analysis**
- Transaction pattern analysis  
- Monthly credit & debit comparison  
- Balance trend visualization  
- Risk indicator assessment  
- Comprehensive PDF report generation  

### **Financial Metrics**
- Total credits & debits  
- Monthly cash flow analysis  
- Average transaction value  
- Highest/lowest transaction amounts  
- Balance fluctuation patterns  

### **Risk Assessment**
- Negative balance day tracking  
- Zero transaction day monitoring  
- Monthly spending patterns  
- Income stability indicators  

### **Visualization**
- Interactive monthly comparison charts  
- Transaction type distribution pie charts  
- Color-coded statistical cards  
- Responsive design  

## 🛠️ Tech Stack
- **Backend:** Python Flask  
- **Frontend:** HTML, TailwindCSS, Font Awesome  
- **Data Processing:** Pandas  
- **Visualization:** Matplotlib  
- **PDF Generation:** FPDF  
- **Styling:** Custom CSS  

## 📋 Prerequisites
- Python 3.8+  
- pip (Python package manager)  
- Modern web browser  
- Basic command-line knowledge  

## 🚀 Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/bank-statement-analyzer.git  
cd bank-statement-analyzer  

# Create a virtual environment (recommended)
python -m venv venv  
# On Windows
.\venv\Scripts\activate  
# On macOS/Linux
source venv/bin/activate  

# Install dependencies
pip install -r requirements.txt  

# Run the application
python app.py  
```

## 📂 Project Structure
```
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
```

## 💡 Use Cases

### **Loan Officers**
- Quick borrower financial assessment  
- Standardized analysis  
- Risk factor identification  
- Loan documentation support  

### **Financial Advisors**
- Client financial behavior analysis  
- Income & spending pattern recognition  
- Professional report generation  

### **Credit Analysts**
- Creditworthiness evaluation  
- Cash flow & transaction pattern study  
- Risk assessment  

### **Small Business Lenders**
- Business cash flow & revenue analysis  
- Seasonality & working capital assessment  

## 🔒 Security Features
- Secure file upload handling  
- Temporary file storage with auto-cleanup  
- No permanent data storage  
- Client-side file validation  
- Server-side file type verification  

## 🔄 Process Flow
1. User uploads a bank statement  
2. System validates the file format  
3. Data processing & analysis  
4. Interactive visualizations generated  
5. Comprehensive PDF report created  
6. Analysis dashboard displayed  
7. Option to download the full report  

## 🚀 Future Enhancements

### **Advanced Analysis**
- Machine learning for pattern recognition  
- Anomaly & fraud detection  
- Industry-specific analysis  

### **Additional Features**
- Multiple statement comparison  
- Custom date range analysis  
- Recurring payment detection  

### **User Experience**
- Dark mode & multi-language support  
- Mobile app version  
- Custom report templates  

### **Integration Capabilities**
- API endpoints for third-party integration  
- Direct bank feed support  
- Export to multiple formats  
- Cloud storage integration  

## 🙏 Acknowledgments
- Flask, Pandas & Matplotlib Documentation  
- TailwindCSS Community  
- Font Awesome Icons  






