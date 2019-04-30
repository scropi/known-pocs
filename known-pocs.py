from selenium import webdriver
import time
import re
def search_poc(keyword):
   headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }

   str1=""
   #print(soup.prettify()).
   option = webdriver.ChromeOptions()
   option.add_argument("headless")   #不打开浏览器
   name=[]
   poc_id=[]
   page=1

   while(page<=10):
     #try:
      print("[+]正在爬取第"+str(page)+"页")
      req = webdriver.Chrome(chrome_options=option)
      print("https://www.seebug.org/search/?keywords=CMS&category=&level=all&has_poc=true&page="+str(page))
      req.get("https://www.seebug.org/search/?keywords=CMS&category=&level=all&has_poc=true&page="+str(page))
      req.refresh()
      page=page+1
      time.sleep(10)    #给js执行时间10s
      #print(req.page_source)
      t=1
      word = []
      while t <=10:

        t=str(t)
        word.append(req.find_elements_by_css_selector(str1.join("body > div.container > div > div > div.table-responsive > table > tbody > tr:nth-child("+t+") > td.vul-title-wrapper > a")))
        t=int(t)
        print(word[t - 1][0].text)
        print(word[t - 1][0].get_attribute('href'))
        #try:
        download(word[t - 1][0].text, word[t - 1][0].get_attribute('href'))
        #except:
            #pass
        #print(word[t-1].extend())
        t=t+1
    # except:
        # print("[-]第"+str(page)+"页爬取出错！")
        # pass
def download(name,url):
    poc_id=re.search("ssvid-.*",url).group().strip("ssvid-")
    #print(poc_id)
    final="https://www.seebug.org/vuldb/downloadPoc/"+poc_id
    print(final)
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    req2 = webdriver.Chrome(chrome_options=option)
    req2.get(final)
    time.sleep(10)
    poc_text=req2.page_source
    print("please wait")

    print(poc_text)
    with open("./"+name+".poc","w")as f:
        f.writelines(poc_text)
        f.close()
#def download_poc(poc_name):


if __name__=="__main__":
    keyword=""
    search_poc(keyword)
