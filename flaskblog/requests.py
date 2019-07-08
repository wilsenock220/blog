import urllib.request,json

def get_quotes():
   '''
   Function that gets the json response to our url request
   '''
   get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

   with urllib.request.urlopen(get_quotes_url) as url:
       quotes = url.read()
       get_sources_response = json.loads(quotes)
       print(quotes)

   return get_sources_response