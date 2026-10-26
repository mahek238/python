import requests
url = 'https://www.example.com/image.jpg'
r = requests.get(url)
with open('image.jpg', 'wb') as f:
 f.write(r.content)