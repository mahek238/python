import requests
url = 'https://example.com'
r = requests.get(url)
with open('page_source.html', 'w', encoding='utf-8') as f:
 f.write(r.text)