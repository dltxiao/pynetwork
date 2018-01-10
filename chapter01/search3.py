#!/usr/bin/env python3

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
	path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
	print(path)
	connection = http.client.HTTPConnection('maps.googleapis.com')
	connection.request('GET', path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print(type(reply))
	print(reply)
	print(reply['results'][0]['geometry']['location'])

if __name__ == '__main__':
	geocode('207 N. Defiance St, Archbold, OH')
