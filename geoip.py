import requests

def get_geo_info(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json")
        data = res.json()
        return data.get("city", ""), data.get("country", "")
    except:
        return "", ""
