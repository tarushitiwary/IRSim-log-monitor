from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from geoip import get_geo_info
from visualizer import plot_attempts

def generate_html_report(failed_attempts):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report.html")

    enriched = {}
    for ip, times in failed_attempts.items():
        city, country = get_geo_info(ip)
        enriched[ip] = {
            "count": len(times),
            "location": f"{city}, {country}"
        }

    plot_attempts(failed_attempts, save_as="static/chart.png")

    html = template.render(
        attempts=enriched,
        generation_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)

