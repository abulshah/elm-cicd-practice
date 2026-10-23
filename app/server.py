import os

APP_VERSION = os.getenv("APP_VERSION", "1.0")

def get_version():
    return APP_VERSION

def get_status():
    return 200
