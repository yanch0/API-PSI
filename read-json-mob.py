import json
import requests
import gspread

gc = gspread.service_account(filename='creds.json')
wks = gc.open("SheetsTest").sheet1
wks.update('A1:J1', [['url', 'score', 'fcp', 'speed ind', 'time to interactive']])

f = open('file.txt', 'r')
count = 1
while True:
    count += 1
    x = f.readline()
    a = x.replace('\n', '')
    if not a:
        break

    url = str("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://" + a + "/&strategy=mobile&locale=en&key=AIzaSyCb3u9C1oiKokdEkRtjPOGp_FZVwbVQh4g")

    response = requests.get(url)
    data = json.loads(response.text)

    requrl = data["lighthouseResult"]["requestedUrl"]
    overall_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100

    fcp = data["lighthouseResult"]["audits"]["metrics"]["details"]["items"][0]['firstContentfulPaint'] / 1000 #First Contentful Paint
    si = data["lighthouseResult"]["audits"]["metrics"]["details"]["items"][0]['speedIndex'] / 1000 #Speed Index
    tti = data["lighthouseResult"]["audits"]["metrics"]["details"]["items"][0]['interactive'] / 1000  #Time To Interactive

    fcp_1 = round(fcp, 1)
    si_1 = round(si, 1)
    tti_1 = round(tti, 1)

    print(requrl)
    print(overall_score)
    print(fcp_1)
    print(si_1)
    print(tti_1)

    cell = 'A' + str(count)
    wks.update(cell, [[requrl, overall_score, fcp_1, si_1, tti_1]])
