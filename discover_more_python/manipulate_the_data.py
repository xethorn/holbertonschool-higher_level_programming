import json
from urllib2 import Request, urlopen, URLError

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 7e573dd60371dc91c35929139cdca698e477e85c'
}

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
	response = urlopen(request)
	read_file = json.loads(response.read())
    #the parsed read_file is selecting the first key and iterating i which holds the first subdirectory
        for i in read_file['items']:
            print i['full_name']
        #print (read_file['items'][x]['full_name']) just a good example of how to select subdirectories
except URLError, e:
    print 'No file. Got an error code:', e
