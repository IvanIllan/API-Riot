from RiotAPI import RiotAPI

def main():
	api = RiotAPI('RGAPI-50243412-7c12-4043-844c-77773a52e424')
	name = 'MonkaS Gun Kelly'
	r = api.get_summoner_by_name(name)
	Matchs = api.get_matchs(r['accountId'])
	lista_matchs = Matchs['matches']
	mid = 0
	bot = 0
	jungler = 0
	top = 0
	none = 0
	for a in range(len(lista_matchs)):
		#print lista_matchs[a]['lane']
		if lista_matchs[a]['lane'] == 'TOP':
			top = top+1
		elif lista_matchs[a]['lane'] == 'JUNGLE':
			jungler = jungler+1
		elif lista_matchs[a]['lane'] == 'MID':
			mid = mid+1
		elif lista_matchs[a]['lane'] == 'BOTTOM':
			bot = bot+1
		elif lista_matchs[a]['lane'] == 'NONE':
			none = none+1
	print "Hola",name
	print "Tu nivel es ",r['summonerLevel']
	print "Has jugado de top",top, "veces en las ultimas 100 partidas"
	print "Has jugado de jungler",jungler, "veces en las ultimas 100 partidas"
	print "Has jugado de mid",mid, "veces en las ultimas 100 partidas"
	print "Has jugado de bot",bot, "veces en las ultimas 100 partidas"
	print "No se ha identificado el rol en:",none ,"situaciones"
if __name__ == "__main__":
	main()

#https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/mazorcon69?api_key=RGAPI-50243412-7c12-4043-844c-77773a52e424
#{u'profileIconId': 3887, u'name': u'mazorcon69', u'puuid': u'54RbniYDQjhp7qannRrIdZ6mLUWDkMqLfcjDrCK4NzaEtu0gv1OanqPlb2CvHGRAZEdAoLABz-yoFA', u'summonerLevel': 65, u'accountId': u'feCKXZ2t_-pX5a2_pRqqHIm_2HU5UjsnjufkR2EESiM6KBw', u'id': u'IK-N51FrADAu3LC2ZxmsiILUIib60RPsvHKmHLoxAjboptg', u'revisionDate': 1545413401000}
#{u'matches': [{u'lane': u'JUNGLE', u'gameId': 3870117682, u'champion': 121, u'platformId': u'EUW1', u'timestamp': 1545329071235, u'queue': 400, u'role': u'NONE', u'season': 11}
