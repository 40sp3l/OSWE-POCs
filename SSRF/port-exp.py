import requests
from colorama import Fore

url = "http://127.0.0.1:5001/"

for port in range(3299, 65535):
    payload = {"url":f"http://127.0.0.1:{port}"}
    exp = requests.post(url, data=payload).text
    if "Read timed out" in exp or "Connection aborted" in exp:
       print("[+] ", port, Fore.GREEN+"Is open"+Fore.WHITE)
       break
    else:
       print(port, "Is closed")
