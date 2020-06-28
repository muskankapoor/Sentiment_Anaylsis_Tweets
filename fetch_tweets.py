import tweepy
import csv


# authentication tokens
consumer_key = 'gNVF7jHVY0ey7IFb3QXjfUuLh'
consumer_secret = 'gHOBoGOCvW0JLREPo49P9dgbBFv5hvQlftbExjHTziBnnOLO4e'
access_token = '1272309012000919552-OqjqeaO0dtLrNhBn9jz9veJV1MmlKW'
access_token_secret = '12OofbRTVGEHiFs4BLYih2i0n4QFUblTk50EYxAlSXQYS'

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token, access_token_secret)
api_access = tweepy.API(authenticate,wait_on_rate_limit=True)

# i used the csv file to kind of provide a format
#csv_file = open('example.csv', 'a')
#csv_write = csv.writer(csv_file)

for tweet in tweepy.Cursor(api_access.search,q="#KylieJenner",count=10, lang="en", since="2020-05-01").items():
    print (tweet.created_at, tweet.text)
    #csv_write.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
      

       
