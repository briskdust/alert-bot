from dotenv import load_dotenv
import requests
import os

load_dotenv()
REQ_URL = os.getenv("REQ_URL")

# The alert message
alert_payload = {
    "content": os.getenv("ALERT_MSG")
}

header = {
    "authorization": os.getenv("REQ_HEADER")
}


def send_msg():
    """
    Sends a message to a discord server
    """
    requests.post(REQ_URL, data=alert_payload, headers=header)
