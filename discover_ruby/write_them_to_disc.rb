#!/usr/bin/ruby
require 'HTTPClient'

extheaders = {
  'User-Agent' => 'Holberton_school',
  'Authorization' => '5b0fbcd1114ea6d6c375c414f1d48d87ef0b71bb'
}

http = HTTPClient.new

api = http.get_content ('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')

File.write('/tmp/27', api)


puts "The File was saved!"