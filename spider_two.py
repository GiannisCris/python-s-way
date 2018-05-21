import requests
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
print(r.text)

