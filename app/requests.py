import urllib.request,json
from .models import Quote

def get_quote(): 
  '''Function that gets the quote response data'''
  quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
  
  with urllib.request.urlopen(quotes_url) as url: 
    quote_data = url.read()
    quote_url_response = json.loads(quote_data)
    
    if quote_url_response: 
      author = quote_url_response['author']
      quote = quote_url_response['quote']
      
      quote_object = Quote(author,quote)
  return quote_object