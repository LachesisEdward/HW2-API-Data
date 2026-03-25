import requests
import json
import csv

# 抓取資料
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# 儲存為 JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# 儲存為 CSV
with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Email'])
    for user in data:
        writer.writerow([user['id'], user['name'], user['email']])