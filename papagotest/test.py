import os
from dotenv import load_dotenv
import requests
import json

# .env 파일 불러오기
load_dotenv()

CLIENT_ID = os.getenv("client_id")
CLIENT_SECRET = os.getenv("client_secret")

# 확인용 출력
# print("CLIENT_ID:", CLIENT_ID)
# print("CLIENT_SECRET:", CLIENT_SECRET)

text = '파이썬은 재미있습니다.'
url = 'https://papago.apigw.ntruss.com/nmt/v1/translation'
headers = {
    'Content-Type': 'application/json',
    'x-ncp-apigw-api-key-id': CLIENT_ID,
    'x-ncp-apigw-api-key': CLIENT_SECRET
}
data = {'source': 'ko', 'target': 'en', 'text': text}


response = requests.post(url, json.dumps(data), headers=headers) 
print(response)

print(response.text)
print(type(response.text))