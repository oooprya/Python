import urllib.request, json 
with urllib.request.urlopen("http://api_version=2") as url:
    data = json.load(url)

for i in range(16):
    print(f"Название фильма: {data['name'][i]} img: {data['FLM_PIC_S'][i]}")