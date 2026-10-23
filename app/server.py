import os

APP_VERSION = os.getenv("APP_VERSION", "BROKEN")

def get_version():
    return APP_VERSION

def get_status():
    return 200
