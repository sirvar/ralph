import tweepy

# Creds details
# 0 - consumer_key
# 1 - consumer_secret
# 2 - access_token
# 3 - access_token_secret
# 4 - username (ralph8ball)
creds = open("../data/creds.txt").read().split("\n")

auth = tweepy.OAuthHandler(creds[0], creds[1])
auth.set_access_token(creds[2], creds[3])

username = creds[4]

api = tweepy.API(auth)

class mStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		if not self.tweetByMe(status.user.id):
			api.retweet(status.id)

	def tweetByMe(self, userId):
		if (api.me().id == userId):
			return True
		return False

ralphListener = mStreamListener()
ralphStream = tweepy.Stream(auth = api.auth, listener = ralphListener)
ralphStream.filter(track = username)