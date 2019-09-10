import urllib
import json

TOKEN = "b116811bc0fcabec2e8f0d85f251276749b5e0fe"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
    def shorten_url(self,longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN,longurl)
            print("bitly url: ",url)
            response = urllib.request.urlopen(url).read()
            jr = json.loads(response)
            return jr["data"]["url"]
        except Exception as e:
            print(e)
