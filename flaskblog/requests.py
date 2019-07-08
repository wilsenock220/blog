import urllib.request.json

base_url = None




def get_quote():
    get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'


    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

    return get_quote_response

