import tweepy
import time

callback_uri = 'oob'
CONSUMER_KEY = "pQggTND1iEmXaxU6hqBkhFs0B"
CONSUMER_SECRET = "iXbg6MJrN1SKWK1OZFyfHLVgMR8TKloVFv1wwlVvbWEQdf3dFe"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPSqUAEAAAAAh3sIb9UdAjywBdRbcfZC20a19RA%3DVOD0ER3fMHJ88wAtJKpm0SDKWAaNjdJXjq89FSOGd7YKCPwhNT"

ACCESS_KEY = "1236242357814734848-7mSPwv6KBvmcZUiVJAcQWxLOfNgtV2"
ACCESS_SECRET = "fSAzdEODBZU89hwOCtry03TI7d8rSTYDaCTNxN819xzX6"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

# File Handling - Store Tweet ID's for mentions

FILE_NAME = 'seen.txt'
def retrieve_last_id(file_name):
    read_id = open(file_name, 'r')
    last_id = int(read_id.read().strip())
    read_id.close()
    return last_id

def store_id(last_id, file_name):
    write_id = open(file_name, 'w')
    write_id.write(str(last_id))
    write_id.close()
    return

def shaky_auth_user(auth):
    auth.secure = True
    auth_url = auth.get_authorization_url()
    print ('Please authorize: ' + auth_url)
    verifier = input('PIN: ').strip()
    auth.get_access_token(verifier)
    print ("ACCESS_KEY = '%s'" % auth.access_token.key)
    print ("ACCESS_SECRET = '%s'" % auth.access_token.secret)

# Replying to tweets
def listen():
    print("listening to mentions....")
    previous_id = retrieve_last_id("seen.txt")
    mentions = api.mentions_timeline(previous_id, tweet_mode='extended')
    for mention in reversed(mentions):
        store_id(mention.id, 'seen.txt')
        print("@" + mention.user.screen_name + " tweeted → " + mention.full_text)
        api.update_status('Hi @' + mention.user.screen_name + ' sorry can\'t group tweet yet, work in progress!', mention.id)
        print("replied @" + mention.user.screen_name)

while True:
    listen()
    time.sleep(15)







# CONSUMER_KEY = "pQggTND1iEmXaxU6hqBkhFs0B"
# CONSUMER_SECRET = "iXbg6MJrN1SKWK1OZFyfHLVgMR8TKloVFv1wwlVvbWEQdf3dFe"
# BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAPSqUAEAAAAAh3sIb9UdAjywBdRbcfZC20a19RA%3DVOD0ER3fMHJ88wAtJKpm0SDKWAaNjdJXjq89FSOGd7YKCPwhNT"

# ACCESS_KEY = "1236242357814734848-7mSPwv6KBvmcZUiVJAcQWxLOfNgtV2"
# ACCESS_SECRET = "fSAzdEODBZU89hwOCtry03TI7d8rSTYDaCTNxN819xzX6"

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# api = tweepy.API(auth)


# import time
# start = time.time()
# end = time.time()
# print(round((end-start), 3), "seconds")