from flask import Flask, request, send_file
import io
import requests
from reportlab.pdfgen import canvas
app = Flask(__name__)
from model.modelFuncs import generate_report
from model.modelFuncs import create_pdf
from scripts.pen_test import test_connect
from scripts.scan_ports import scan_ports

@app.route('/create_report', methods=['POST'])
def create_report():
    data = request.json
    url = data.get('link')

    if not url:
        return {'error': 'No link provided'}, 400
    
    response = requests.get(url)
    if response.status_code != 200:
        return {'error': 'Failed to retrieve data'}, 500
    print("here")
    pen_test_results = test_connect()
    print("here")
    scan_res = scan_ports(url, 3000)

    
    rep = generate_report(scan_res, pen_test_results)
    create_pdf(rep, cybersecurity_report.pdf)

    return send_file("./cybersecurity_report.pdf", as_attachment=True, download_name="etc")

if __name__ == '__main__':
    app.run(debug=True)