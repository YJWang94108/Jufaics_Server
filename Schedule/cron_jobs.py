import requests
import time

def Run():
    while True:
        PokeMyself()
        time.sleep(600) # 10 min

def PokeMyself():
    headers = {'user-agent':'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    try:
        r = requests.get('https://jufaics-server.onrender.com', headers=headers, verify=False)
        print('[GET]:'+str(r.status_code))
    except Exception as e:
        print('[Error]:'+str(e))
