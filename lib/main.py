import tweepy

creds = open("../data/creds.txt").read().split("\n")

auth = tweepy.OAuthHandler(creds[0], creds[1])
auth.set_access_token(creds[2], creds[3])

api = tweepy.API(auth)
