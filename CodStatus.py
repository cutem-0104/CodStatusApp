# coding:utf-8
import requests
import pprint

domain = 'https://my.callofduty.com'
pass1 = '/api/papi-client/stats/cod/{0}/title/mw/platform/{1}/gamer/{2}/profile/type/{3}'

mp_url = domain + pass1.format('v1', 'battle', 'cutem%231611', 'mp')
mp_get = requests.get(mp_url)

wz_url = domain + pass1.format('v1', 'battle', 'cutem%231611', 'wz')
wz_get = requests.get(wz_url)

def print_mode_stat(json, term, mode):
	print(term + ' ' + mode)
	lifetime_json = json['data'][term]['mode'][mode]['properties']
	print_stat(lifetime_json)

def print_stat(json):
	pprint.pprint('kill : ' + str(json['kills']))
	pprint.pprint('death : ' + str(json['deaths']))
	pprint.pprint('k/d : ' + str(round(json['kdRatio'], 3)))
	pprint.pprint('SPM : ' + str(round(json['scorePerMinute'], 1)))
	try:
		pprint.pprint('time : ' + str(round(json['timePlayedTotal'] / 3600, 1)))
	except KeyError:
		pprint.pprint('time : ' + str(round(json['timePlayed'] / 3600, 1)))
	print()

print('lifetime stat')
print_stat(mp_get.json()['data']['lifetime']['all']['properties'])
print_mode_stat(mp_get.json(), 'lifetime', 'dom')
print_mode_stat(mp_get.json(), 'lifetime', 'war')
print_mode_stat(mp_get.json(), 'lifetime', 'hq')
print_mode_stat(mp_get.json(), 'lifetime', 'conf')
print_mode_stat(mp_get.json(), 'lifetime', 'br_dmz')
print_mode_stat(mp_get.json(), 'lifetime', 'br')

print('weekly stat')
print_stat(mp_get.json()['data']['weekly']['all']['properties'])
print_mode_stat(mp_get.json(), 'weekly', 'dom')
print_mode_stat(mp_get.json(), 'weekly', 'war')
print_mode_stat(mp_get.json(), 'weekly', 'hq')
print_mode_stat(mp_get.json(), 'weekly', 'conf')
print_mode_stat(wz_get.json(), 'weekly', 'br_dmz_38')
print_mode_stat(wz_get.json(), 'weekly', 'br_25')
