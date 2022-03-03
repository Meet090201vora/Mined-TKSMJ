import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re
import string

html_text = requests.get("https://arxiv.org/list/cs.AI/recent",headers={'User-Agent':'Mozilla/5.0'})
soup = bs(html_text.text,'lxml')

article = soup.find("dl")
dds = article.find_all("dd")
dts = article.find_all("dt")


title =[]
authors = []
keyword = []
abstract = []
date = []


for dt in dts:
  link = dt.find("span",class_="list-identifier").a['href']
  link = "https://arxiv.org/" + link

  html_text1 = requests.get(link,headers={'User-Agent':'Mozilla/5.0'})
  soup1 = bs(html_text1.text,'lxml')

  abstract.append(soup1.find("blockquote",class_= "abstract mathjax").text.replace("Abstract:","").replace("\n",""))
  dt = (soup1.find('div',class_="dateline").text.replace("[Submitted on ","").replace("]","").replace("\n",""))
  dt = re.sub(' +', ' ', dt)
  date.append(dt)


for dd in dds:
  ti = (dd.find("div",class_="list-title mathjax").text.replace("Title:","").replace("\n",""))
  ti = ti.translate(str.maketrans('','',string.punctuation))
  ti = re.sub(' +', ' ', ti)
  title.append(ti)

  at = (dd.find("div",class_="list-authors").text.replace("Authors:","").replace("\n",""))
  at = at.translate(str.maketrans('','',string.punctuation))
  at = re.sub(' +', ' ', at)
  authors.append(at)

  keyword.append(dd.find("div",class_="list-subjects").text.replace("Subjects:","").replace("\n",""))

dataf = pd.DataFrame({"Title":title,
              "Authors":authors,
              "Keyword":keyword,
              "Abstract":abstract,
              "Date":date})



dataf.to_csv('rp.csv',index=False)

