import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

html_text = requests.get("https://arxiv.org/list/cs.AI/recent",headers={'User-Agent':'Mozilla/5.0'})
soup = bs(html_text.text,'lxml')

article = soup.find("dl")
dds = article.find_all("dd")
dts = article.find_all("dt")


title =[]
authors = []
keyword = []
abstract = []

for dt in dts:
  link = dt.find("span",class_="list-identifier").a['href']
  link = "https://arxiv.org/" + link

  html_text1 = requests.get(link,headers={'User-Agent':'Mozilla/5.0'})
  soup1 = bs(html_text1.text,'lxml')

  abstract.append(soup1.find("blockquote",class_= "abstract mathjax").text.replace("Abstract:","").replace("\n",""))

for dd in dds:
  title.append(dd.find("div",class_="list-title mathjax").text.replace("Title:","").replace("\n",""))
  authors.append(dd.find("div",class_="list-authors").text.replace("Authors:","").replace("\n",""))
  keyword.append(dd.find("div",class_="list-subjects").text.replace("Subjects:","").replace("\n",""))

dataf = pd.DataFrame({"Title":title,
              "Authors":authors,
              "Keyword":keyword,
              "Abstract":abstract})


dataf.to_csv('rp.csv')