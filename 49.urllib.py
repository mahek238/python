from urllib.request import urlopen
url = 'https://example.com'
resp = urlopen(url)
html = resp.read().decode('utf-8')
with open('downloaded_page.html', 'w', encoding='utf-8') as f:
 f.write(html)