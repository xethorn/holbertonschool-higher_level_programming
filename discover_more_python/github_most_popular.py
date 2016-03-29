from urllib2 import Request, urlopen, URLError

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 7e573dd60371dc91c35929139cdca698e477e85c'
}

request = Request('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc')

try:
	response = urlopen(request)
	read_file = response.read()
	print read_file
except URLError, e:
    print 'No file. Got an error code:', e
