 #app.py
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import tempfile
from datetime import datetime
import os 

app = Flask(__name__)
app.secret_key = 'b19f8c1e76bca8c02e6a2fbe5bd5b9d8'  # Required for flashing messages

# Create directories if they don't exist
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOADS_FOLDER = os.path.join(BASE_DIR, 'uploads')
# REPORTS_FOLDER = os.path.join(BASE_DIR, 'reports')
# STATIC_FOLDER = os.path.join(BASE_DIR, 'static', 'images')
os.makedirs('uploads', exist_ok=True)
os.makedirs('reports', exist_ok=True)
os.makedirs('static/images', exist_ok=True)

# os.makedirs(UPLOADS_FOLDER, exist_ok=True)
# os.makedirs(REPORTS_FOLDER, exist_ok=True)
# os.makedirs(STATIC_FOLDER, exist_ok=True)


def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
    df["Debit (Rs.)"] = pd.to_numeric(df["Debit (Rs.)"], errors="coerce").fillna(0)
    df["Credit (Rs.)"] = pd.to_numeric(df["Credit (Rs.)"], errors="coerce").fillna(0)
    df["Balance (Rs.)"] = pd.to_numeric(df["Balance (Rs.)"], errors="coerce").fillna(0)
    df["Month"] = df["Date"].dt.strftime('%b')
    df["Month_Num"] = df["Date"].dt.month
    return df

def calculate_statistics(df):
    df_sorted = df.sort_values("Month_Num")
    
    stats = {
        'total_credit': df["Credit (Rs.)"].sum(),
        'total_debit': df["Debit (Rs.)"].sum(),
        'net_balance_change': df["Balance (Rs.)"].iloc[-1] - df["Balance (Rs.)"].iloc[0],
        'closing_balance': df["Balance (Rs.)"].iloc[-1],
        'monthly_credit': df_sorted.groupby("Month")["Credit (Rs.)"].sum(),
        'monthly_debit': df_sorted.groupby("Month")["Debit (Rs.)"].sum(),
        'monthly_highest_balance': df_sorted.groupby("Month")["Balance (Rs.)"].max(),
        'monthly_lowest_balance': df_sorted.groupby("Month")["Balance (Rs.)"].min(),
        'transaction_counts': df["Transaction Type"].value_counts(),
        'total_transactions': len(df),
        'avg_transaction': (df["Credit (Rs.)"].sum() + df["Debit (Rs.)"].sum()) / (
            (df["Credit (Rs.)"] != 0).sum() + (df["Debit (Rs.)"] != 0).sum()
        ),
        'largest_credit': df["Credit (Rs.)"].max(),
        'largest_debit': df["Debit (Rs.)"].max(),
        'smallest_credit': df[df["Credit (Rs.)"] > 0]["Credit (Rs.)"].min(),
        'smallest_debit': df[df["Debit (Rs.)"] > 0]["Debit (Rs.)"].min(),
        'busiest_day': df.groupby("Date").size().idxmax().strftime('%d-%m-%Y'),
        'highest_spending_month': df_sorted.groupby("Month")["Debit (Rs.)"].sum().idxmax(),
        'lowest_spending_month': df_sorted.groupby("Month")["Debit (Rs.)"].sum().idxmin(),
        'highest_income_month': df_sorted.groupby("Month")["Credit (Rs.)"].sum().idxmax(),
        'lowest_income_month': df_sorted.groupby("Month")["Credit (Rs.)"].sum().idxmin(),
        'negative_balance_days': (df["Balance (Rs.)"] < 0).sum(),
        'zero_transaction_days': ((df["Credit (Rs.)"] == 0) & (df["Debit (Rs.)"] == 0)).sum(),
    }
    return stats

def create_charts(stats):
    # Monthly Credit vs Debit Chart
    plt.figure(figsize=(10, 5))
    months = stats['monthly_credit'].index
    x = range(len(months))
    plt.bar(x, stats['monthly_credit'], width=0.35, label='Credit', color='green', alpha=0.7)
    plt.bar([i+0.35 for i in x], stats['monthly_debit'], width=0.35, label='Debit', color='red', alpha=0.7)
    plt.xlabel("Month")
    plt.ylabel("Amount (Rs.)")
    plt.title("Monthly Credit & Debit Comparison")
    plt.legend()
    plt.xticks([i+0.175 for i in x], months, rotation=45)
    # plt.savefig(os.path.join(STATIC_FOLDER, 'monthly_comparison.png'), bbox_inches='tight')
    plt.savefig('static/images/monthly_comparison.png', bbox_inches='tight')
    plt.close()

    # Transaction Type Distribution
    plt.figure(figsize=(8, 8))
    stats['transaction_counts'].plot(kind='pie', autopct='%1.1f%%')
    plt.title("Transaction Type Distribution")
    # plt.savefig(os.path.join(STATIC_FOLDER, 'transaction_distribution.png'), bbox_inches='tight')
    plt.savefig('static/images/transaction_distribution.png', bbox_inches='tight')
    plt.close()


def generate_pdf_report(stats, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Bank Statement Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # General Overview Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. General Overview", ln=True)
    pdf.set_font("Arial", "", 12)
    
    # Key Statistics in a grid-like layout
    stats_data = [
        ["Total Credit", f"Rs. {stats['total_credit']:,.2f}"],
        ["Total Debit", f"Rs. {stats['total_debit']:,.2f}"],
        ["Closing Balance", f"Rs. {stats['closing_balance']:,.2f}"],
        ["Total Transactions", str(stats['total_transactions'])]
    ]
    
    for label, value in stats_data:
        pdf.cell(95, 8, label, border=1)
        pdf.cell(95, 8, value, border=1, ln=True)
    pdf.ln(10)

    # Visual Analysis Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Visual Analysis", ln=True)
    
    # Add monthly comparison chart
    pdf.image('static/images/monthly_comparison.png', x=10, w=190)
    pdf.ln(5)
    pdf.image('static/images/transaction_distribution.png', x=10, w=190)
    pdf.ln(10)

    # Transaction Analysis Section
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "3. Transaction Analysis", ln=True)
    pdf.set_font("Arial", "", 12)
    
    transaction_data = [
        ["Total Transactions", str(stats['total_transactions'])],
        ["Average Transaction", f"Rs. {stats['avg_transaction']:,.2f}"],
        ["Largest Credit", f"Rs. {stats['largest_credit']:,.2f}"],
        ["Largest Debit", f"Rs. {stats['largest_debit']:,.2f}"]
    ]
    
    for label, value in transaction_data:
        pdf.cell(95, 8, label, border=1)
        pdf.cell(95, 8, value, border=1, ln=True)
    pdf.ln(10)

    # Monthly Trends Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "4. Monthly Trends", ln=True)
    pdf.set_font("Arial", "", 12)
    
    monthly_data = [
        ["Highest Income Month", stats['highest_income_month']],
        ["Highest Spending Month", stats['highest_spending_month']],
        ["Busiest Day", stats['busiest_day']]
    ]
    
    for label, value in monthly_data:
        pdf.cell(95, 8, label, border=1)
        pdf.cell(95, 8, value, border=1, ln=True)
    pdf.ln(10)

    # Risk Indicators Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "5. Risk Indicators", ln=True)
    pdf.set_font("Arial", "", 12)
    
    risk_data = [
        ["Negative Balance Days", str(stats['negative_balance_days'])],
        ["Zero Transaction Days", str(stats['zero_transaction_days'])]
    ]
    
    for label, value in risk_data:
        pdf.cell(95, 8, label, border=1)
        pdf.cell(95, 8, value, border=1, ln=True)

    pdf.output(output_filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file and file.filename.endswith('.csv'):
            # Save uploaded file
            # upload_path = os.path.join(UPLOADS_FOLDER, 'bank_statement.csv')
            upload_path = os.path.join('uploads', 'bank_statement.csv')

            file.save(upload_path)
            
            try:
                # Process the data
                df = load_and_process_data(upload_path)
                stats = calculate_statistics(df)
                
                # Create charts
                create_charts(stats)
                
                # Generate PDF report
                # report_path = os.path.join(REPORTS_FOLDER, 'Bank_Statement_Analysis.pdf')
                report_path = os.path.join('reports', 'Bank_Statement_Analysis.pdf')
                generate_pdf_report(stats, report_path)
                
                return render_template('report.html', stats=stats)
            
            except Exception as e:
                flash(f'Error processing file: {str(e)}')
                return redirect(request.url)
        else:
            flash('Please upload a CSV file')
            return redirect(request.url)
    
    return render_template('index.html')

@app.route('/download_report')
def download_report():
    report_path = os.path.join('reports', 'Bank_Statement_Analysis.pdf')
    if os.path.exists(report_path):
        return send_file(report_path, as_attachment=True, download_name=f'Bank_Statement_Analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf')
    else:
        flash('Report not found. Please generate the report first.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)