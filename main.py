#!/usr/bin/env python

from dotenv import load_dotenv

import requests

import os

# Load configuration from .env
load_dotenv()

SSL_TEST_URL = os.getenv("SSL_TEST_URL") 
SERVER_NAME = os.getenv("SERVER_NAME")

ONLINE_BASE_URL = f"http://{SERVER_NAME}/24online"
LOGIN_URL = ONLINE_BASE_URL + "/servlet/E24onlineHTTPClient"

PROFILE_NAME = os.getenv("PROFILE_NAME")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")



def do_it():
    try:
        requests.get("https://example.com")
        print("Already logged in; Doing nothing.")
    except requests.exceptions.SSLError:
        # We have a problem, let's fix it!

        print("Attempting to log in..")

        r = requests.post(
            LOGIN_URL,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Upgrade-Insecure-Requests": "1"
            },

            # These are the minimal sets of arguments required to send a login request
            data={
                "mode": 191,
                "logintype": "2",
                "servername": SERVER_NAME,
                "profilegroupid": "1",
                "profileName": PROFILE_NAME,
                "username": USERNAME,
                "password": PASSWORD,
            }
        )

        # Check if we were successful
        if not "You have successfully logged in" in r.text:
            return print("Failed to login.")

        print("Login attempt successful. Enjoy!")

if __name__ == "__main__":
    do_it()
