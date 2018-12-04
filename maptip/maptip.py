import urllib
import urllib2
import json
from qgis.core import *
from qgis.gui import *

@qgsfunction(args="auto", group="Custom")
def wikipediaSummary(name, feature, parent):
	baseurl = 'https://en.wikipedia.org/w/api.php?'
	params={
			'action': 'query',
			'format': 'json',
			'titles': name,
			'prop': 'extracts',
			'exintro': True,
			'explaintext': True,
			}
	url = baseurl + urllib.parse.urlencode(params)

	response = urllib2.urlopen(url)
	if response.getcode() != 200:
		return "No wikipedia entry was found"
	sresults = response.read()
	results = json.loads(sresults)
	extract = list(results['query']['pages'].values())[0]['extract']
	return extract
