__author__ = "Foster Gorman"

import requests
import smtplib
import argparse
import re
from bs4 import BeautifulSoup
from datetime import datetime

parser = argparse.ArgumentParser(description='Automatically email your public IP at 7 AM and 12 PM')
parser.add_argument('-s', '--from_email', type=str, required=True, help='Email address you want the email to be sent from')
parser.add_argument('-t', '--token', type=str, required=True, help='Token required to send the email')
parser.add_argument('-r', '--to_email', type=str, help='Email address you want to send the IP to. Defaults to from_email')

args = parser.parse_args()
from_email = args.from_email
to_email = args.from_email
token = args.token

from_email_regex = r'[\w\.]+@gmail\.com$'
to_email_regex = r'[\w\.]+@([\w-]+\.)+[a-zA-Z]{2,4}$'

if not re.match(from_email_regex, from_email):
    print('Invalid from email address. Currently only supporting Gmail.')
    exit()

if args.to_email:
    to_email = args.to_email
    if not re.match(to_email_regex, to_email):
        print("Invalid to email address format.")
        exit()

while True:
    current_time = str(datetime.now())
    current_time = current_time[11:22]

    if current_time == "07:00:00.00" or current_time == "12:00:00.00":
        mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        mail_server.ehlo()
        mail_server.login(email, token)

        request = requests.get("http://whatismyip.host/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find("p", {"class": "ipaddress"})
        public_ip = element.text.strip()

        msg = "Your public IP at home is {0}".format(public_ip)
        mail_server.sendmail(from_email, to_email, msg)
        mail_server.quit()