__author__ = "Foster Gorman"

import requests, smtplib
from bs4 import BeautifulSoup
from datetime import datetime

print("EmailPublicIP.py is running")

while True:
    current_time = str(datetime.now())
    current_time = current_time[11:22]

    if current_time == "07:00:00.00" or current_time == "12:00:00.00":
        mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        mail_server.ehlo()
        mail_server.login("mh337.fg@gmail.com", "wrvllkleoomzfodv")

        request = requests.get("http://whatismyip.host/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find("p", {"class": "ipaddress"})
        public_ip = element.text.strip()

        msg = "Your public IP at home is {0}".format(public_ip)
        mail_server.sendmail("mh337.fg@gmail.com", "mh337.fg@gmail.com", msg)
        mail_server.quit()

        print("Email was sent")


# <span id="priceblock_ourprice" class="a-size-medium a-color-price">$137.19</span>