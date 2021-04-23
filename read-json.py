import json
import requests

f = open('file.txt', 'r')
x = f.readline()
a = x.replace('\n', '')

url = str("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://" + a + "/&strategy=mobile&locale=en&key=AIzaSyCb3u9C1oiKokdEkRtjPOGp_FZVwbVQh4g")
print(url)

response = requests.get(url)
print(response)
data = json.loads(response.text)

print(data == response.json())
print(type(data))

overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100

fcp = data["lighthouseResult"]["audits"]["metrics"]["details"]["items"][0]['firstContentfulPaint'] / 1000 #First Contentful Paint
si = data["lighthouseResult"]["audits"]["metrics"]["details"]["items"][0]['speedIndex'] / 1000 #Speed Index
# tti = #Time To Interactive

print(overall_score)
print(fcp)
print(si)