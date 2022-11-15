import requests
from lxml import etree
url = 'https://www.toolbaba.cn/ip'


headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

}

resp = requests.get(url,headers= headers)
resp.encoding = 'gbk'

e = etree.HTML(resp.text)
ips = e.xpath('//div[1]/table//tr//td[1]/text()')
ports = e.xpath('//div[1]/table//tr//td[2]/text()')
addrs = e.xpath('//div[1]/table//tr//td[3]/text()')
with open('IP代理地址.txt','w') as f:
    for i,p,a in zip(ips,ports,addrs):
        f.write(f'IP地址:{i}----port端口号:{p}----地址:{a}\n')