import urllib as req
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response:
    data = response.read().decode("utf-8")
print(data)

# "stitle":景點名稱, "address":區域,"longitude":經度, "latitude":緯度, "file": 第一張圖檔網址
