import urllib
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
	try:
		response = urllib.request.urlopen(url)  
		sresults = response.read()
		results = json.loads(sresults)
		extract = list(results['query']['pages'].values())[0]['extract']
		return extract
	except Exception:
		return "No wikipedia entry was found"
			
