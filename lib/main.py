import tweepy
import random

# Creds details
# 0 - consumer_key
# 1 - consumer_secret
# 2 - access_token
# 3 - access_token_secret
# 4 - username (ralph8ball)
creds = open("../data/creds.txt").read().split("\n")

# OAuth
auth = tweepy.OAuthHandler(creds[0], creds[1])
auth.set_access_token(creds[2], creds[3])

username = creds[4]

api = tweepy.API(auth)

# Reply options
options = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

# Tweepy StreamListener tracks mentions to username
class mStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		if not self.tweetByMe(status.user.id):
			api.retweet(status.id)
			self.reply(status)

	# Check if tweet is made by me
	def tweetByMe(self, userId):
		if (api.me().id == userId):
			return True
		return False

	# Replys to tweet with random option
	def reply(self, tweet):
		rand = random.randint(0, len(options))
		api.update_status(".@" + tweet.user.screen_name + " " + options[rand], tweet.id)

# Init StreamListener
ralphListener = mStreamListener()
ralphStream = tweepy.Stream(auth = api.auth, listener = ralphListener)
# Listen for tweets with username
ralphStream.filter(track = ["@" + username])