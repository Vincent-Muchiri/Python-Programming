from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = "data/credentials.json"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

