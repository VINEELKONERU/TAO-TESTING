
    # TODO implement
import requests
    #global alist
    #prod url = 'http://infpwesch101.ad.unsw.edu.au/Scientia/Portal'
url = 'http://taotesting.test.unsw.edu.au:89'

    #print "url is" + url
try:
  
    r = requests.get(url)
    print r.status_code
    #print r

except:

    print "error executing"
