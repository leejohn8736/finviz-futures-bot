import os
import sys
from curl_cffi import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ 텔레그램 설정값(TOKEN 또는 CHAT_ID)이 없습니다.")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    
    response = requests.post(url, data=data)
    print(f"📡 응답 코드: {response.status_code}")
    print(f"📡 응답 내용: {response.text}")

def main():
    site_url = "https://finviz.com/futures"
    message = (
        "📊 <b>[Finviz 선물 바로가기]</b>\n\n"
        f"오늘의 선물 현황을 확인해보세요:\n{site_url}"
    )
    
    try:
        send_telegram_message(message)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
