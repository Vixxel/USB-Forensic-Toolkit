# USB Forensic Toolkit

A Python-based digital forensics toolkit for Windows that performs USB artifact collection, timeline reconstruction, case management, SHA256 evidence verification, and automated forensic report generation.

## Features

- USB Registry Analysis
- USB Timeline Reconstruction
- Risk Scoring Engine
- Device Statistics Dashboard
- CSV Export
- JSON Export
- HTML Reports
- PDF Reports
- SHA256 Evidence Hashing
- Chain of Custody Logging
- Colorized Terminal Interface

## Requirements

- Python 3.10+
- Windows

## Installation

```bash
git clone https://github.com/Vixxel/USB-Forensic-Toolkit

cd USB-Forensic-Toolkit

pip install -r requirements.txt

python main.py
```

## requirements.txt

```text
colorama>=0.4.6
reportlab>=4.0.0
pywin32>=306
```

```text
USB-Forensic-Toolkit/

main.py

modules/
├── registry_parser.py
├── risk_engine.py
├── statistics.py
├── export_utils.py
├── hash_utils.py
├── html_report.py
├── pdf_report.py
├── timeline.py
├── chain_of_custody.py
├── case_manager.py

requirements.txt
README.md
```

## Future Features

- Case Management System
- Timeline Export
- Device Fingerprinting
- Investigation Notes
- Automatic Hash Logging
- Dashboard Overview

## Author

Vixxel / Vexa
Cybersecurity & Digital Forensics
