import tweepy 

  
class TwitterAPI(object): 
    
    def __init__(self): 
        
        # i would need some keys and authentication information here 
        # attempt authentication 
        try: 
           # try something
        except: 
            print("Error: Authentication Failed") 
            
  
    def GetTweets(self, query, count = 10): 
        
        # empty list to store parsed tweets 
        tweets = [] 
        
        try: 
            fetched_tweets = self.api.search(q = query, count = count) 
            

            for tweet in fetched_tweets: 
                
                tweet = {} 
                
                parsed_tweet['text'] = tweet.text 
                 
                if tweet.retweet_count > 0: 
                   
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
                    
            return tweets 
        
        except tweepy.TweepError as e: 
            print("Error : " + str(e)) 
            
def main(): 

    api = TwitterAPI() 
    tweets = api.get_tweets(query = 'Donald Trump', count = 100) 
    
 
  
if __name__ == "__main__": 
    main() 
