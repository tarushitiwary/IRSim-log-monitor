# IRSim - Incident Response Simulation Tool

**IRSim** is a command-line cybersecurity tool that simulates real-time log monitoring and basic incident response scenarios. It parses Apache log files, detects brute-force attacks, identifies geo-locations of attackers, and generates analytical reports.

---

## 🚀 Features

- 🔍 **Brute-force Detection** from Apache access logs
- 🌍 **GeoIP Lookup** of source IPs using `ipinfo.io`
- 📊 **Data Visualization** with matplotlib (charts of IP activity)
- 📑 **HTML Report Generation** (templated reports)
- 🔄 **Real-Time Log Monitoring** (tail-like detection using Watchdog)
- 🐳 **Dockerized** for platform-diagnostic deployment
- 🛠️ CLI Support using `argparse`

---

## 🛠️ Installation

### 🔧 Requirements
- Python 3.10+
- pip
- Docker (optional)

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### Run 
```bash
python -m venv venv
.\venv\Scripts\activate
python main.py --logfile sample_logs/access.log --report
start .\report.html

