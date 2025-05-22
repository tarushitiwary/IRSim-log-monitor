
# 🛡️ IRSim – Building a Python-Based Incident Response Simulation Tool

## 🔍 **Introduction**

As a final-year Computer Science student with a passion for cybersecurity and backend development, I wanted to create a project that would demonstrate my ability to **analyze security incidents, automate threat detection**, and **visualize findings** — all using Python.

That’s how **IRSim (Incident Response Simulation)** was born.

IRSim is a CLI-based cybersecurity tool that:
- Parses Apache web server logs
- Detects brute-force login attempts
- Maps suspicious IPs to their geographic locations
- Visualizes attack data using bar charts
- Generates HTML reports with visual summaries
- Runs seamlessly inside a Docker container

## ⚙️ **Why I Built This**

Most cybersecurity incidents start with subtle clues in logs — repeated login failures, spikes in traffic, or activity from unusual IPs. My goal was to build a tool that could simulate how a Security Engineer might:
- Investigate suspicious activity
- Automate repetitive log checks
- Generate forensic reports

This project helped me tie together everything I've learned — from **regex parsing and API integration to data visualization, modular Python architecture, and Dockerization.**

## 🧱 **Tech Stack**
- 🐍 **Python** for scripting and modular design
- 📊 **Matplotlib** for charting
- 🌍 **IPInfo API** for GeoIP lookup
- 🖼️ **Jinja2** for HTML templating
- 🐳 **Docker** for deployment
- 📁 Apache log simulation with real-world format

## 🔬 **How It Works**

### 1. 📜 **Log Parsing**
The tool reads Apache access logs and extracts key info — IP address, timestamp, and status codes. Only failed login attempts (`401`) are analyzed using a regular expression.

```python
pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\] "POST /login.*" (\d+)')
```

### 2. 🚨 **Brute-Force Detection**
It flags IPs with 3 or more failed login attempts. This threshold is configurable using CLI flags.

### 3. 🌍 **GeoIP Mapping**
Each suspicious IP is sent to `ipinfo.io`, and the resulting country/city info is added to the report.

### 4. 📊 **Visualization**
A bar chart shows the number of failed attempts per IP — making it easier to visually interpret threat sources.

### 5. 📝 **Report Generation**
All data is embedded into an HTML report, including:
- A detailed table of alerts
- Geo-location info
- Attack chart
- Generation timestamp

### 6. 🐳 **Docker Support**
With a `Dockerfile`, IRSim is packaged for any platform. No messy dependency installations — just build and run.

## 🧪 **Sample CLI Commands**

```bash
# Basic log analysis
python main.py --logfile sample_logs/access.log

# With report generation
python main.py --logfile sample_logs/access.log --report

# Custom brute-force threshold
python main.py --logfile sample_logs/access.log --threshold 5
```

## 📁 **Project Structure**
- `log_parser.py` – Reads and extracts failed login entries
- `alerts.py` – Detects brute-force IPs
- `geoip.py` – Maps IPs to locations
- `visualizer.py` – Generates attack charts
- `report_gen.py` – Renders and exports an HTML report
- `main.py` – CLI interface
- `Dockerfile` – For containerized execution

## 💡 **What I Learned**

- How real-world incident response starts with basic log data
- The value of modular architecture in Python projects
- Working with APIs (like IPInfo) to enrich data
- Designing user-friendly CLI interfaces with `argparse`
- Packaging and deploying with Docker

## 🧠 **What’s Next?**
Future enhancements I’m planning:
- Real-time log monitoring with `watchdog`
- PDF report export
- Slack/email alert integrations
- Basic anomaly detection using a machine learning model
  

## 🙋‍♂️ About Me
I'm a final-year B.Tech CSE student passionate about security, automation, and backend engineering. IRSim is part of my journey to become a Security Engineer, blending hands-on problem-solving with automation-first thinking.
