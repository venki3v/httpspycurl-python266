import pycurl
import cStringIO
response = cStringIO.StringIO()
conn = pycurl.Curl()
conn.setopt(pycurl.VERBOSE, 1)
conn.setopt(pycurl.URL, "https://dummy.com/dummy.py")
conn.setopt(pycurl.SSL_VERIFYPEER, False)
conn.setopt(pycurl.SSL_VERIFYHOST, False)
conn.setopt(pycurl.WRITEFUNCTION, response.write)
conn.perform()
http_code = conn.getinfo(pycurl.HTTP_CODE)
print http_code
if http_code is 200:
   print response.getvalue()
