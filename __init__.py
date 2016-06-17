'''
import urllib.request
import time

start = time.time()
url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download'
response = urllib.request.urlopen(url)
exportHere = response.read()

with open('export.csv', 'wb') as f:
    f.write(exportHere)

end = time.time()
print('Time elapsed %.2f sec' % (end - start))
'''

import time
from datetime import datetime, timedelta

while 1:
    print('Run something...')
    dt = datetime.now() + timedelta(seconds=10)
    while datetime.now() < dt:
        time.sleep(5)
