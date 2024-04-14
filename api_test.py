import requests
import json
from datetime import datetime

def main():
    url = "http://localhost:8000/contacts"
    current_time = datetime.now().isoformat()
    body = {"id": 1, 
            "name": "string", 
            "email": "user@example.com", 
            "url": "http://example.com", 
            "gender": 0, 
            "message": "string",
            "is_enabled": False,
            "created_at": current_time
            }
    
    res = requests.post(url, json.dumps(body)) #requestは辞書型では送信できないので、json形式で送信
    print(body)
    print(json.dumps(body))
    print(res.json()) # json形式で受信

# 直接このファイルが実行された場合のみmain()を実行
if __name__ == "__main__":
    main()