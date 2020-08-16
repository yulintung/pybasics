import requests

r = requests.get("https://www.bing.com")
print(r.status_code)
print(r.text)

newFile = open("./requestDemo.txt", "w+")
newFile.write(r.text)
