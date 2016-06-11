# Ralph
Meet Ralph, the magic 8 ball bot on Twitter! 

Ralph is a Twitter bot who works like a magic 8 ball. You tweet at him to ask him a yes or no question and he will reply with a magic answer.

Try it out! [@ralph8ball](https://twitter.com/ralph8ball)

## Installation
Firstly, make sure you have tweepy

`$ pip3 install tweepy`

Then, add your own credentials in `data/creds.txt` from your [Twitter App](https://apps.twitter.com/)
###### Line 1 - consumer_key
###### Line 2 - consumer_secret
###### Line 3 - access_token
###### Line 4 - access_token_secret
###### Line 5 - username (ralph8ball)

Finally, run Ralph by

`$ cd lib`

`$ python3 main.py`