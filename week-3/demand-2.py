import urllib.request as req
def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    txt1=''
    txt2=''
    txt3=''
    for title in titles:
      if title.a != None:
        # print(title.a.string)
        if title.a.string[1:3] == "好雷":
          txt1+=title.a.string+"\n"
        elif title.a.string[1:3] == "普雷":
          txt2+=title.a.string+"\n"
        elif title.a.string[1:3] == "負雷":
          txt3+=title.a.string+"\n"
    nextLink=root.find("a", string="‹ 上頁")
    return nextLink["href"], txt1, txt2, txt3


# 主程序：抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/movie/index.html"
# print(getData(pageURL))
conut=0
txt1=''
txt2=''
txt3=''
while conut<10:
  pageURL = "https://www.ptt.cc" + getData(pageURL)[0]
  conut+=1
  txt1+=getData(pageURL)[1]
  txt2+=getData(pageURL)[2]
  txt3+=getData(pageURL)[3]

with open("movie.txt", "w") as file:
  file.write(txt1)
  file.write(txt2)
  file.write(txt3)
