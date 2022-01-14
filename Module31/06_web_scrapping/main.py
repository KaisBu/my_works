import requests
import re


my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
veb_text = my_req.text

all_heads3 = re.findall(r"<h3.*>.*<", veb_text)
all_heads3 = [re.search(r'>.*<', i_head).group(0)[1:-1] for i_head in all_heads3]
print(all_heads3)



