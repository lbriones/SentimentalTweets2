from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json

#conn = MySQLdb.connect("localhost","root","lagwagon","beginneraccount$tutorial")

#c = conn.cursor()


#consumer key, consumer secret, access token, access secret.
ckey="NhKXNHp5u9yTtNZdmHGs5NCtd"
csecret="LKHqoFsCCAnPZGe9IXEkwpCv0LQVvdtvRJSqPkKnKpuILr22ml"
atoken="523419774-rXzTBTkVQW6XqO7vimDhSf5l6TgAPiJAwuyiN13t"
asecret="yncMCCkfPPwz0d22BfszVVamKiQ5b1Os7fkn4mCTNduqx"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        if  not all_data["text"].startswith('RT'):
            #Do processing here 
            #tweet = all_data["text"].encode('utf8')
            
            screen_name                     = all_data["user"]["screen_name"]
            screen_id                       = all_data["user"]["id"]
            #profile_background_image_url    = all_data["user"]["profile_background_image_url"]
            #geo                             = all_data["geo"]
            
            #c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            #(time.time(), username, tweet))
            #conn.commit()
    
            print(screen_id, str(screen_name))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Justin Bieber"])
