from fastapi import FastAPI, Request
from pydantic import BaseModel
import psutil
import re
import subprocess
import os
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

class ServerMonitoringSDK:
    """ A class that provides server monitoring capabilities such as system metrics, website health check, and listing websites. """
    
    def __init__(self):
        pass

    def check_website_health(self, url: str) -> str:
        """Checks if a website is up and returns its status."""
        try:
            response = requests.get(url, timeout=5)
            return f"Website {url} is up with status code {response.status_code}."
        except requests.exceptions.RequestException:
            return f"Website {url} is down or unreachable."

    def get_system_metrics(self) -> dict:
        """Returns the system metrics including CPU, memory, disk usage, and temperature."""
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        temperature = psutil.sensors_temperatures().get('coretemp', [])[0].current if psutil.sensors_temperatures() else "N/A"
        return {
            "cpu_usage": f"{cpu_usage}%",
            "memory_usage": f"{memory.percent}%",
            "disk_usage": f"{disk.percent}%",
            "temperature": f"{temperature}°C"
        }

    def list_websites(self) -> str:
        """Lists websites running on the server by checking Nginx and Apache configurations."""
        websites = []

        # Check for Nginx running process
        try:
            nginx_config_path = "/etc/nginx/sites-enabled"
            if os.path.exists(nginx_config_path):
                for file in os.listdir(nginx_config_path):
                    with open(os.path.join(nginx_config_path, file), 'r') as f:
                        content = f.read()
                        server_names = re.findall(r"server_name\s+([^;]+);", content)
                        websites.extend(server_names)
        except Exception as e:
            websites.append(f"Error checking Nginx: {str(e)}")

        # Check for Apache running process
        try:
            apache_output = subprocess.check_output(["apachectl", "-S"], stderr=subprocess.STDOUT, text=True)
            for line in apache_output.splitlines():
                if "namevhost" in line:
                    websites.append(line.split()[0])
        except subprocess.CalledProcessError as e:
            websites.append(f"Error checking Apache: {str(e.output)}")
        except FileNotFoundError:
            websites.append("Apache not installed or not running.")

        return "Websites running on server:\n" + "\n".join(websites) if websites else "No websites found."


# Create an instance of the SDK
sdk = ServerMonitoringSDK()

@app.post("/check-website-health")
async def website_health_endpoint(request: Request):
    data = await request.json()
    url = data.get("url", "https://djserver.live/")
    response_text = sdk.check_website_health(url)
    return {"response": response_text}

@app.get("/system-metrics")
async def system_metrics_endpoint():
    metrics = sdk.get_system_metrics()
    return {
        "cpu_usage": metrics['cpu_usage'],
        "memory_usage": metrics['memory_usage'],
        "disk_usage": metrics['disk_usage'],
        "temperature": metrics['temperature']
    }

@app.get("/list-websites")
async def list_websites_endpoint():
    response_text = sdk.list_websites()
    return {"response": response_text}
