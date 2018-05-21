import requests
url = "https://www.zhihu.com/people/qia-zi-26/activities"
try:
    kv = {'user-agent':'mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("error")

