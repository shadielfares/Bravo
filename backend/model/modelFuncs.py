import os
from dotenv import load_dotenv
import openai
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

def generate_report(vulnerability_data):
    prompt = f"Generate a detailed cybersecurity report based on these vulnerabilities:\n{vulnerability_data}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose other models if preferred
        prompt=prompt,
        max_tokens=1000,
        temperature=0.5
    )
    return response.choices[0].text.strip()

sample_data = """
Vulnerability: SQL Injection
Severity: High
Description: Allows SQL code injection through user inputs.
Recommendation: Implement input validation and use parameterized queries.
"""
print(generate_report(sample_data))

def create_pdf(report_text, file_path="cybersecurity_report.pdf"):
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

