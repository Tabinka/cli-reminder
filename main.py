import datetime
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ntfy_url = os.getenv("NTFY_URL")

reminded_prompt = input("What should I remind you of? ")

print(f"Ok I will remind you of: {reminded_prompt}")

date_prompt = input("When it should be reminded? (YYYY-MM-DD HH:MM) ")

print(f"Ok, I will remind you about it in this time: {date_prompt}")

datetime_object = datetime.datetime.strptime(date_prompt, "%Y-%m-%d %H:%M")
timestamp = datetime_object.timestamp()

print("Reminder was set!")

while (time.time() <= timestamp):
      time.sleep(1)

if ntfy_url:
      requests.post(ntfy_url, data=f"{reminded_prompt} 😀".encode(encoding='utf-8'))
else:
      print("URL was not correct.")

exit()