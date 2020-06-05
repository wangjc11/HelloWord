import requests
import parsel
response = requests.get("http://www.shuquge.com/txt/8659/2324752.html")
response.encoding = response.apparent_encoding
print(response.text)
sel = parsel.Selector(response.text)
h1 = sel.css('#content::text')
print(h1.getall())