import datetime
import re
import requests
import smtplib
import sched, time
import threading
import os
from dotenv import load_dotenv
load_dotenv()


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

websiteUrl = {
    'URL' : os.getenv("siteAddr")
}

loginInfo = {
    'sender' : os.getenv("senderEmail"),
    'receiver' : os.getenv("receiverEmail"),
    'password' : os.getenv("senderPass")
}
print(loginInfo.get('sender'))
statusesCodes = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}

def send_email(message):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(loginInfo.get('sender'), loginInfo.get('password'))
        server.sendmail(loginInfo.get('sender'), loginInfo.get('receiver'), message)

        return "Сообщение успешно отправлено"
    except Exception as _ex:
        return f"{_ex}\nПроверь логин или пароль"


def check_site():
    threading.Timer(1800.0, check_site).start()    # перезапуск каждые N секунд
    # urls = websiteUrl.values();
    for url in websiteUrl.values():
        try:
            web_response = requests.get(url)
            print(url, statusesCodes[web_response.status_code])
            print(time.ctime())
            print(send_email(message="OMR still working!"))

        except:
            print(url, statusesCodes[web_response.status_code])
            print(time.ctime())
            print(send_email(message="OMR having some troubles:("))

check_site()
#print(send_email(message="OMR still working!"))
