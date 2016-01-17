import requests
import re
import pdfkit

#please contact me if I am infringing any copyright by writting this script.
source_url = 'http://www.geeksforgeeks.org/c-plus-plus/'

r = requests.get(source_url)
string = r.text
lists = re.findall(r'<ul>(.*?)</ul>', string, re.DOTALL|re.MULTILINE)
k=0
total = 0

for i in lists:
	k += 1
	if k > 22:
		break
	elif k == 1:
		continue
	else:
		new_lists = re.findall(r'href="(.*?)"', i, re.DOTALL|re.MULTILINE)
		for j in new_lists:
			try:
				#total += 1
				#if total > 66:
					#print j
				file_name  = 'c++_notes/' + str(j[29:len(j)-1]) + '.pdf'
				pdfkit.from_url(str(j), file_name)

			except:
				print str(j)
				print total
				break
