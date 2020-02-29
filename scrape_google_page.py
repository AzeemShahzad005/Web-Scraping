import urllib
import requests
from bs4 import BeautifulSoup

# Desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "pakistan"
query = query.replace(' ', '+')
URL = "https://www.google.com/search?ei=wpNOXq26J5Gl1fAPouqp4AE&q="+str(query)+"&oq=" + str(query);
print(URL)

headers = {"user-agent": USER_AGENT}
print(headers)
resp = requests.get(URL, headers=headers)
print(resp.status_code)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                title: title,
                link: link
            }
            results.append(item)
    print(results)
    result = []
    for g in soup.find_all('div', class_='s'):
        span = g.find_all('span')
        if span:
            snippet = g.find('span').text
            item = {
                snippet: snippet,
            }
            result.append(item)
    print(result)
