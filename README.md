# HackMe

## Description
HackMe is designed to help startups ensure the safety of their websites by conducting comprehensive security assessments. The application performs port scans and brute-force SSH tests to identify potential vulnerabilities, allowing companies to address security issues proactively and read the results by a well-formatted report.

## Features
- 🛡️ **Port Scanning**: Identifies open ports on the target system.
- 🔐 **Brute-force SSH Testing**: Attempts multiple login combinations to test for weak credentials.
- 📊 **Report Generation**: Provides detailed reports on identified vulnerabilities.
- 🖥️ **User-friendly Interface**: Easy-to-use React frontend for managing scans and viewing results.

## Getting Started
Follow these steps to set up and run the application.

### Setting Up the Backend
1. Ensure `pip` is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the penetration test:
   ```bash
   python3 backend/scripts/pen-test.py
   ```
4. Run the port scan:
   ```bash
   python3 backend/scripts/scan-ports.py
   ```

### Setting Up the Frontend
1. Navigate to the frontend directory:
   ```bash
   cd front-end/mec
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React application:
   ```bash
   npm start
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser to view the application.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

For more information, visit the [HackMe repository](https://github.com/shadielfares/HackMe).
