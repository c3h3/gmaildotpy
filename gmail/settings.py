"""
please place a file gmail_settings.py

GMAIL_ACCOUNT = ""
GMAIL_PASSWORD = ""

or set the environment variables

GMAIL_ACCOUNT = ""
GMAIL_PASSWORD = ""

"""

try:
    from gmail_settings import GMAIL_ACCOUNT
except:
    GMAIL_ACCOUNT = "default_account"
    
try:
    from gmail_settings import GMAIL_PASSWORD
except:
    GMAIL_PASSWORD = "default_password"
    
import os

GMAIL_ACCOUNT = os.environ.get("GMAIL_ACCOUNT", GMAIL_ACCOUNT)
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD", GMAIL_PASSWORD)
