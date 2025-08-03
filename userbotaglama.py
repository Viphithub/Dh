from pyrogram import Client, filters
from asyncio import sleep

api_id = 25091293
api_hash = "80feec30ed5c238fcee14cdf96d84d9c"
owner_id = 6077249114

app = Client("userbot", api_id=api_id, api_hash=api_hash)

aktif_gruplar = {}  # hangi gruplarda aktif
ozel_yazi = "free pubg cloud private"  # mesajın sonu
link = "@Darkstorm1bot @Darkstorm1bot"  # mesajın başı

@app.on_message(filters.command("basla") & filters.user(owner_id))
async def baslat(client, message):
    chat_id = message.chat.id
    aktif_gruplar[chat_id] = True
    await message.reply("✅ Etiketleme başlatıldı (6 kişi/mesaj)")

    etiket_listesi = []

    try:
        async for u in app.get_chat_members(chat_id):
            if not aktif_gruplar.get(chat_id):
                break
            if u.user.is_bot or u.user.is_deleted:
                continue

            mention = (
                f"@{u.user.username}"
                if u.user.username
                else f"[{u.user.first_name}](tg://user?id={u.user.id})"
            )

            etiket_listesi.append(mention)

            if len(etiket_listesi) == 6:
                metin = f"{link}\n\n" + " ".join(etiket_listesi) + f"\n\n{ozel_yazi}"
                await app.send_message(chat_id, metin)
                etiket_listesi.clear()
                await sleep(2)  # 2 saniye bekle

        # Kalan kullanıcılar
        if etiket_listesi:
            metin = f"{link}\n\n" + " ".join(etiket_listesi) + f"\n\n{ozel_yazi}"
            await app.send_message(chat_id, metin)

    except Exception as e:
        await message.reply(f"❌ Hata oluştu: {e}")


@app.on_message(filters.command("kapa") & filters.user(owner_id))
async def durdur(client, message):
    chat_id = message.chat.id
    aktif_gruplar[chat_id] = False
    await message.reply("⛔ Etiketleme durduruldu.")


@app.on_message(filters.command("yaz") & filters.user(owner_id))
async def yazi_degistir(client, message):
    global ozel_yazi
    if len(message.command) < 2:
        await message.reply("❗ Yeni yazıyı belirt: `/yaz mesaj`")
        return
    ozel_yazi = " ".join(message.command[1:])
    await message.reply(f"✅ Yeni mesaj ayarlandı:\n\n`{ozel_yazi}`")


print("🔄 Userbot başlatılıyor...")
app.run()