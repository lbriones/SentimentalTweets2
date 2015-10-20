from django.core.management.base import BaseCommand, CommandError
from twperson.models import UserTw, Status
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
# Create your views here.
ckey="NhKXNHp5u9yTtNZdmHGs5NCtd"
csecret="LKHqoFsCCAnPZGe9IXEkwpCv0LQVvdtvRJSqPkKnKpuILr22ml"
atoken="523419774-rXzTBTkVQW6XqO7vimDhSf5l6TgAPiJAwuyiN13t"
asecret="yncMCCkfPPwz0d22BfszVVamKiQ5b1Os7fkn4mCTNduqx"
# Create your views here.
class listener(StreamListener):

	def on_data(self, data):
		all_data = json.loads(data)
		if not all_data["text"].startswith('RT') and bool(all_data["text"].strip()) is not False:
			#Do processing here 
			text 		= all_data["text"].encode('utf8')
			screen_name = all_data["user"]["screen_name"]
			screen_id = all_data["user"]["id"]
			screen_description = all_data["user"]["description"]
			userTw, created = UserTw.objects.get_or_create(screen_name=screen_name, screen_id=screen_id, description=screen_description)
			if created:
				# A new person object created
				status = Status(text=text, usertw=userTw)
				status.save()
				#TODO add keyworkd from alchemylanguage "keywords": [{"relevance": "0.904619","text": "Justin Bieber"}
				#TODO add docSentiment from alchemylanguage "docSentiment": [{"score": "0.522221","type": "positive"}
				#TODO add tweets from twitter 
				
			else:
				# person object already exists
				status = Status(text=text, usertw=userTw)
				status.save()
				#TODO add keyworkd from alchemylanguage "keywords": [{"relevance": "0.904619","text": "Justin Bieber"}
				#TODO add docSentiment from alchemylanguage "docSentiment": [{"score": "0.522221","type": "positive"}
				#TODO add tweets from twitter 

			return True

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Justin Bieber"])