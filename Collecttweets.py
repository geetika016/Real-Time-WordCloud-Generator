from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sys
import unicodedata as ud


#Variables that contains the user credentials to access Twitter API 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#Print Tweets
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data["text"]
            #username = all_data["user"]["screen_name"]
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            #tweet = tweet.decode('utf8')
            print(tweet.translate(non_bmp_map))
            #print(BMP(tweet))
            #print(tweet)
            savefile = open("d:\\wk.txt", "a", encoding='utf-8')
            savefile.write(tweet)
            savefile.write("\n")
            savefile.close()
        except(BaseException ,e):
            print("Failed on Data", str(e))
            time.sleep(5)
        #return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['#Hashtag'])
    
 

