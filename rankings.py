from requests import get
from pprint import PrettyPrinter
from config import CFBD_API_KEY

BASE_URL = "https://apinext.collegefootballdata.com"
url = f"{BASE_URL}/teams/fbs"
headers = {"Authorization": f"Bearer {CFBD_API_KEY}"}

response = get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    printer = PrettyPrinter(depth=4, width=120)
    printer.pprint(data)
else:
    print("Error:", response.status_code)
    print(response.text)