import requests
import time
import sys
from fake_useragent import UserAgent

def banner():
    print("[+]===============================[+]")
    print("[+]       UNICH Airdrop Bot       [+]")
    print("[+]      Clear task & Mining      [+]")
    print("[+]       @AirdropFamilyIDN       [+]")
    print("[+]===============================[+]")

def info_akun(token):
    ua = UserAgent()
    url = "https://api.unich.com/airdrop/user/v1/info/my-info"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": ua.random,
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://unich.com",
        "Referer": "https://unich.com/",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if data.get("code") == "OK":
        email = data['data']['email']
        email_parts = email.split('@')
        email_sensored = email_parts[0][:5] + '****' + '@' + email_parts[1]
        print(f"Email: {email_sensored}")
    else:
        print(f"Failed to retrieve account info. Message: {data.get('message')}")

def start_mining(token):
    ua = UserAgent()
    url = "https://api.unich.com/airdrop/user/v1/mining/start"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": ua.random,
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://unich.com",
        "Referer": "https://unich.com/",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": '"Android"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    response = requests.post(url, headers=headers)
    data = response.json()
    if data.get("code") == "OK":
        print("Mining started successfully.")
    else:
        print(f"Failed to start mining. Message: {data.get('message')}")

def cek_mining(token):
    ua = UserAgent()
    url = "https://api.unich.com/airdrop/user/v1/mining/recent"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": ua.random,
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://unich.com",
        "Referer": "https://unich.com/",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": '"Android"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if data.get("code") == "OK":
        mining_status = data['data']['isMining']
        daily_reward = data['data']['miningDailyReward']
        print(f"Mining status: {mining_status}, Daily reward: {daily_reward}")
    else:
        print(f"Failed to check mining status. Message: {data.get('message')}")

def read_tokens_from_file():
    with open('token.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_random_username():
    url = "https://api.randomuser.me/"
    response = requests.get(url)
    data = response.json()
    username = data['results'][0]['login']['username']
    return username

def get_social_list_by_user(token):
    ua = UserAgent()
    url = "https://api.unich.com/airdrop/user/v1/social/list-by-user"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": ua.random,
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://unich.com",
        "Referer": "https://unich.com/",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    item_ids = []
    if data.get("code") == "OK":
        items = data.get("data", {}).get("items", [])
        for item in items:
            item_id = item.get("id")
            item_ids.append(item_id)
    else:
        print("Failed to retrieve data")
    return item_ids

def clear_task(token, item_id, evidence):
    ua = UserAgent()
    url = f"https://api.unich.com/airdrop/user/v1/social/claim/{item_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": ua.random,
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://unich.com",
        "Referer": "https://unich.com/",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    payload = {"evidence": evidence}
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    if data.get("code") == "OK":
        print(f"Task {item_id} cleared successfully. Points rewarded: {data['data']['pointReward']}")
    elif data.get('message') == "You already claim this quest":
        print(f"Task {item_id} already claimed.")
    else:
        print(f"Failed to clear task {item_id}. Message: {data.get('message')}")
    time.sleep(5)

def process_account(token):
    info_akun(token)
    start_mining(token)
    cek_mining(token)
    item_ids = get_social_list_by_user(token)
    evidence = get_random_username()
    for item_id in item_ids:
        clear_task(token, item_id, evidence)

def main():
    try:
        banner()
        tokens = read_tokens_from_file()
        total_tokens = len(tokens)
        print(f"Total akun: {total_tokens}\n")
        
        hours_to_run = int(input("Masukkan loop dalam jam: "))
        end_time = time.time() + hours_to_run * 3600
        
        while time.time() < end_time:
            for index, token in enumerate(tokens, start=1):
                print(f"Memproses akun {index}/{total_tokens}")
                process_account(token)
                print("================================")
            
            
            while time.time() < end_time:
                remaining_time = end_time - time.time()
                hours, remainder = divmod(remaining_time, 3600)
                minutes, seconds = divmod(remainder, 60)
                sys.stdout.write(f"\rMenunggu selama {int(hours):02}:{int(minutes):02}:{int(seconds):02} sebelum loop berikutnya.")
                sys.stdout.flush()
                time.sleep(1)
            
            print("\nLoop berikutnya dimulai.")
            
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()