from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
import MySQLdb
import datetime
from twperson.models import UserTw, Status

# Create your views here.
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
from twitter import Twitter, OAuth, TwitterHTTPError
import os

def search_tweets(q, count=100, result_type="recent"):
	"""
	    Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	"""
	t = Twitter(auth=OAuth(atoken, asecret, ckey, csecret))

	return t.search.tweets(q=q, result_type=result_type, count=count)


def user_timeline(q, count=200, result_type="recent"):
	"""
	    Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	"""
	t = Twitter(auth=OAuth(atoken, asecret, ckey, csecret))

	return t.statuses.user_timeline(screen_name=q, result_type=result_type, count=count)





#!/usr/bin/env python

#	Copyright 2013 AlchemyAPI
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
from __future__ import print_function
from alchemyapi import AlchemyAPI
import json


demo_text = 'Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one.'
demo_url = 'http://www.npr.org/2013/11/26/247336038/dont-stuff-the-turkey-and-other-tips-from-americas-test-kitchen'
demo_html = '<html><head><title>Python Demo | AlchemyAPI</title></head><body><h1>Did you know that AlchemyAPI works on HTML?</h1><p>Well, you do now.</p></body></html>'
image_url = 'http://demo1.alchemyapi.com/images/vision/football.jpg'

# Create the AlchemyAPI Object
alchemyapi = AlchemyAPI()

response = alchemyapi.keywords('text', demo_text, {'sentiment': 1})

if response['status'] == 'OK':
    print('## Response Object ##')
    print(json.dumps(response, indent=4))

    print('## Keywords ##')
    for keyword in response['keywords']:
        print('text: ', keyword['text'].encode('utf-8'))
        print('relevance: ', keyword['relevance'])
        print('sentiment: ', keyword['sentiment']['type'])
        if 'score' in keyword['sentiment']:
            print('sentiment score: ' + keyword['sentiment']['score'])
        print('')
else:
    print('Error in keyword extaction call: ', response['statusInfo'])
"""






def dashboard(request):
	tweets_hashtag = search_tweets('DondeComienzaelCambio')
	count           = tweets_hashtag['search_metadata']['count']
	for user in range(int(count)):
		if not tweets_hashtag['statuses'][int(user)]['text'].startswith('RT'):
			user_text 			= tweets_hashtag['statuses'][int(user)]['text'].encode('ascii', 'ignore')

			user_id 			= tweets_hashtag['statuses'][int(user)]['user']['id']
			user_screen_name 	= tweets_hashtag['statuses'][int(user)]['user']['screen_name'].encode('ascii', 'ignore')
			user_description 	= tweets_hashtag['statuses'][int(user)]['user']['description']
			user_timelinen		= user_timeline(user_screen_name)
			user_timelinen		= [tweet['text'].encode('ascii', 'ignore') for tweet in user_timelinen if not tweet['text'].encode('ascii', 'ignore').startswith('RT')]
			#obtener personalidad desde los twittes 
			#for timeline in range(len(timelines)):
			#    print timelines[timeline]['text']
			#userTw, created = UserTw.objects.get_or_create(screen_name=user_screen_name, screen_id=user_id, description=user_description, timeline=user_timelinen)
			
			#llamar a watson
			#TODO add personality from watson "keywords": [{"relevance": "0.904619","text": "Justin Bieber"}
			#TODO add tweets from twitter 
			userTw, created = UserTw.objects.update_or_create(
					screen_name=user_screen_name, 
					screen_id=user_id, 
					description=user_description, 
					timeline=user_timelinen, 
					defaults={
						'screen_name': user_screen_name,
						'screen_id': user_id,
						'description': user_description,
						'timeline': user_timelinen,
						},
				)
			if created:
				userTw.description = user_description
			else:
				userTw.description = user_description
			#llamar a alchemy
			#TODO add keyworkd from alchemylanguage "keywords": [{"relevance": "0.904619","text": "Justin Bieber"}
			#TODO add docSentiment from alchemylanguage "docSentiment": [{"score": "0.522221","type": "positive"}
			#TODO add tweets from twitter 
			status, created = Status.objects.get_or_create(text=user_text, usertw=user_screen_name)
			"""
			if created:
				# A new person object created
				status = Status(text=user_text, usertw=userTw)
				status.save()
			else:
				# person object already exists
				status = Status(text=user_text, usertw=userTw)
				status.save()
			"""
	users = UserTw.objects.all()
	status 	= Status.objects.all()
	context = {"users": users, "status": status}
	return render(request, "index.html", context)


def home(request):
	users = UserTw.objects.all().count
	status 	= Status.objects.all().count
	context = {"users": users, "status": status}

	return render(request, "home.html", context)



