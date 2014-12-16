import urllib
import re

#TItile scrap of any website 

# regex='<title>(.+?)</title>'
# pattern =re.compile(regex)

# htmlfile = urllib.urlopen("https://www.cnn.com")
# htmltext=htmlfile.read()
# titles=re.findall(pattern,htmltext)
# print titles

# Scrap using finance yahoo.com

# symbolfile=open("symbols.txt")
# symbolslist=symbolfile.read()
# newsymbolslist=symbolslist.split("\n")
# # symbolslist=["APPL","SPY"]
# i=0
# while i<len(newsymbolslist)-1:
# 	url="http://finance.yahoo.com/q?s="+newsymbolslist[i]+"&ql=1"
# 	htmlfile=urllib.urlopen(url)
# 	htmltext=htmlfile.read()
# 	regex='<span class="time_rtq_ticker">(.+?)</span></span>'
# 	pattern=re.compile(regex)
# 	price=re.findall(pattern,htmltext)
# 	s=price[0]
# 	print s.split(">",1)[1] 
# 	i+=1

# Scrap using google finance

htmltext=urllib.urlopen("http://www.google.com/finance?q=AAPL")

regex='<span id="ref_[^.]*_l">(.+?)</span>'
pattern=re.compile(regex)
results=re.findall(pattern,htmltext)
print results
