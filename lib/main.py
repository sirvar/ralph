import tweepy
import random

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

options = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

class mStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		if not self.tweetByMe(status.user.id):
			api.retweet(status.id)
			self.reply(status)

	def tweetByMe(self, userId):
		if (api.me().id == userId):
			return True
		return False

	def reply(self, tweet):
		rand = random.randint(0, len(options))
		api.update_status(".@" + tweet.user.screen_name + " " + options[rand], tweet.id)

ralphListener = mStreamListener()
ralphStream = tweepy.Stream(auth = api.auth, listener = ralphListener)
ralphStream.filter(track = [username])