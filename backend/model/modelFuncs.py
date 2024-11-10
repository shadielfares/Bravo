import os
from dotenv import load_dotenv
import openai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

def generate_report(port_scan_results, vulnerability_results):

    response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can choose other models if preferred
            messages = [{"role": "user", "content": f"Generate a detailed cybersecurity report based on these brute force credential attempt results:{vulnerability_results}, and these port scan results: {port_scan_results}"}],
            max_tokens=1000,
            temperature=0.5
            )
    return response['choices'][0]['message']['content']

sample_data = """
Vulnerability: SQL Injection
Severity: High
Description: Allows SQL code injection through user inputs.
Recommendation: Implement input validation and use parameterized queries.
"""


def create_pdf(report_text, file_path="./cybersecurity_report.pdf"):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, "Cybersecurity Report")

    # Add report text
    text = c.beginText(100, height - 150)
    text.setFont("Helvetica", 12)
    text.setLeading(14)
    text.textLines(report_text)
    c.drawText(text)

    # Save the PDF
    c.save()

