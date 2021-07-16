import requests
import argparse
from bs4 import BeautifulSoup


cliparse = argparse.ArgumentParser()
cliparse.add_argument("-d", "--domain", help="Targeted domain", dest="t_domain")
cliparse.add_argument("-u", "--user-agent", help="Select user agent string", dest="agent_select")
args = cliparse.parse_args()

agent_s = args.agent_select

header_ff = {
    "User-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0"
}
header_ch = {
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
header_op = {
    "User-agent":"Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2"
}
header_sa = {
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"
}

if agent_s == "firefox":
    header = header_ff
elif agent_s == "chrome":
    header == header_ch
elif agent_s == "opera":
    header == header_op
elif agent_s == "safari":
    header == header_sa
else:
    header = header_ff

def pycord():
    print("PermanentPycord by lawsecnet v0.1/n")

    domain = args.t_domain
    page = requests.get("https://" + domain, headers=header)

    soup = BeautifulSoup(page.content, "lxml")

    print(soup.text)

pycord()