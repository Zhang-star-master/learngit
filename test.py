import urllib
import re
url = 'https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny'
s = urllib.urlopen(url).read()
correnprice1 = re.search('(?<=buy":")(\d+.\d+)', s, flags=0)
print correnprice1
correnprice = correnprice1.group()
print correnprice