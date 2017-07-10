import ujson as json
import requests
import geocoder
from app.settings import WEATHER_USERNAME as U, WEATHER_PASSWORD as P

WEATHER_URL = 'https://{}:{}@twcservice.eu-gb.mybluemix.net/api/weather/'.format(U, P)

def weather(city):
	try:
		#if (data['entities'][0]['disambiguation']['subtype'][0]) == 'City':
		#	if data['concepts'][0]['text'] == 'Weather' and data['concepts'][0]['relevance'] >= .9: 
		response = requests.get(
			'{}v3/location/search?query={}&language=en-US'.format(
				WEATHER_URL, 
				city,#data['entities'][0]['text']
				)
			)
		r = response.json()
		g = geocoder.google(
			[
			r['location']['latitude'][0], 
			r['location']['longitude'][0]], method='reverse'
			)
		response = requests.get(
			'{}v1/geocode/{}/{}/forecast/daily/7day.json'.format(
				WEATHER_URL, 
				r['location']['latitude'][0], 
				r['location']['longitude'][0]
				)
			)
		response = response.json()
		r = 'by day: ' + str(response['forecasts'][0]['narrative']) + ', at night: ' + str(response['forecasts'][0]['night']['narrative'])
		return r
	except:
		pass
		