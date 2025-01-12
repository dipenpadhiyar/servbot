from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    server_url: Optional[str] = None  # Server URL provided by the user

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    """
    Main chat endpoint that handles user queries and sends appropriate API
    calls to the specified server running the ServerMonitoringSDK.
    """
    message = chat_request.message.lower()
    server_url = chat_request.server_url

    if not server_url:
        return {"response": "Please provide the server URL to query."}

    try:
        if "cpu usage" in message or "system metrics" in message:
            response = requests.get(f"{server_url}/system-metrics")
            return {"response": response.json()}
        
        elif "list websites" in message or "running websites" in message:
            response = requests.get(f"{server_url}/list-websites")
            return {"response": response.json()}
        
        elif "check website" in message or "website health" in message:
            # Extract the URL from the message (basic example)
            url = "https://example.com"  # Default URL if none provided
            if "http" in message:
                url_start = message.find("http")
                url_end = message.find(" ", url_start) if " " in message[url_start:] else len(message)
                url = message[url_start:url_end]
            
            response = requests.post(f"{server_url}/check-website-health", json={"url": url})
            return {"response": response.json()}
        
        else:
            return {"response": "I'm not sure how to help with that. Please try asking about system metrics, websites, or website health."}
    
    except requests.exceptions.RequestException as e:
        return {"response": f"Failed to connect to server: {e}"}

@app.get("/")
async def root():
    return {"message": "Ollama Chatbot is running!"}
