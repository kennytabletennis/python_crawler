# scratch a PTT HTML from NTU beautiful block
import urllib.request as req
def getData(url):
    #create a object of request wiht Request Headers's information
    request=req.Request(url, headers={
        
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # decode the origin code, To get the title of each article
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")#Let BeautifulSoup help us to decode Html doc
    contents=root.find_all("div", class_="content")#search all class="title" div labels

    for content in contents:
        if content.pre  : #if title include a label, print it
            print(title.a.string)
    # catch previous page
    nextLink=root.find("a", string="下一篇")#Find out the context include "‹ 上頁"
    return print(nextLink["href"])
#catch title of pages
pageurl="https://www.lawplus.com.tw/#reportDetail?id=CYDM,109,%E5%98%89%E7%B0%A1,1220,20201012,1-f1d4782f-4f2c-4168-b902-5c7a4e82ce3f"
count=0
while count<227:
    getData(pageurl)
    count+=1