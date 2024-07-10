# Made with ❤ by yummy
import requests
import time
from colorama import init, Fore, Style
import sys
import os
init(autoreset=True)

def print_welcome_message():
    print(r"""
            jamet
          """)


    print(Fore.GREEN + Style.BRIGHT + "CROSSSFI")
    print(Fore.GREEN + Style.BRIGHT + "Telegram: @hisha\n")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_credentials():
    try:
        with open('tokens.txt', 'r') as file:
            credentials_list = file.readlines()
        credentials = [cred.strip() for cred in credentials_list]
        return credentials
    except FileNotFoundError:
        print("File 'tokens.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script.")
        return []

def telegram(apikey, authorization):
    url = 'https://testpad.xfi.foundation/api/v1/authenticate/telegram'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://bot.crossfi.org',
        'dnt': '1',
        'Referer': 'https://bot.crossfi.org/',
        'priority': 'u=1, i',
        'Sec-Ch-Ua': '"Not A;Brand";v="99", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-mobile': '?1',
        'Sec-Ch-Ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
}
    data = {}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

