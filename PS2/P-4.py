import requests
from datetime import datetime
import urllib3

# Disable warnings about unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
    "https://www.google.com",
    "https://example.com/nonexistent"
]

def check_app_health(url):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Bypass SSL verification
        response = requests.get(url, timeout=5, verify=False)
        if response.status_code == 200:
            print(f"[{timestamp}] Application is UP: {url}")
        else:
            print(f"[{timestamp}] Application is DOWN: {url} (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] Application is DOWN: {url} (Error: {e})")

if __name__ == "__main__":
    for url in urls:
        check_app_health(url)
