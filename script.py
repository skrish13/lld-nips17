
import requests
from bs4 import BeautifulSoup


parent_url = 'https://lld-workshop.github.io/'

page = requests.get(parent_url)
c = page.content
soup = BeautifulSoup(c)
all_links = soup.find_all("a")
print('Total Papers Found:{}'.format(len(all_links)))
count = len(all_links)
current = 1
for link in all_links:
	try:
		dl = link.attrs['href']
		current+=1
		if dl.endswith('pdf'):
			if 'papers' in dl:
				print 'Downloading {}/{}:{}'.format(current, count,  dl)
				import urllib
				urllib.urlretrieve(parent_url + dl, '{}.pdf'.format(current))
	except:
		pass



import os
import subprocess
base = "./"
chunk = os.listdir(base)
print chunk
base_command = 'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/default -dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages -dCompressFonts=true -r150 -sOutputFile=otherone-disentangled_nips17_workshop_book.pdf'
for i in range(0,len(chunk)):
	base_command += " " + base + chunk[i] + " "

print base_command

subprocess.call(base_command)