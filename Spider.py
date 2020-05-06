from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urlparse import urlsplit
from collections import deque
#Senator Was Here
url = raw_input('Entre url:')
new_urls = deque([url])
processed_urls = set()
local_urls = set()
foreign_urls = set()
urlsbroken_urls = set()
while len(new_urls):
    url = new_urls.popleft()
    processed_urls.add(url)
    print('Processing %s' % url)
    useraget = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    try:
        response = requests.get(url, headers=useraget)
    except:
        continue
        broken_urls.add(url)
        continue
    parts = urlsplit(url)
    base = '{0.netloc}'.format(parts)
    strip_base = base.replace('www.', '')
    base_url = '{0.scheme}://{0.netloc}'.format(parts)
    path = url[:url.rfind('/')+1]
    if '/' in parts.path:
        #Coded By Senator
        with open('Senator.txt','ab') as f:
            f.write(url + '\n')

    else:
        url
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a'):
        anchor = link.attrs['href'] if 'href' in link.attrs else ''
        if anchor.startswith('/'):
            Senator = base_url + anchor
            local_urls.add(Senator)
        elif strip_base in anchor:
            local_urls.add(anchor)
        elif not anchor.startswith('http'):
            Senator = path + anchor
            local_urls.add(Senator)
        else:
            foreign_urls.add(anchor)
            for i in local_urls:
                if not i in new_urls and not i in processed_urls:
                    new_urls.append(i)
                    if not link in new_urls and not link in processed_urls:
                        new_urls.append(link)
#feel_Free
