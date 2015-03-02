import tweepy

def authenticate_user():
	try:
		consumer_key="hhYq78kZ6VkAp4Q4pXzuKCOkA"
		consumer_secret="A468W3FnFd9WcL2PXYeRO0iLWnu90761HkKHijXRXqmgtR1bpk"
		access_token="374363728-BCe1rusHWiVPBHDCQ5RoketbfaNePuHXTeJja7W6"
		access_token_secret="cMyNaQwVzxtXKqSG0jjlI1H6avEoMbvZ36pB7Zr5dPEN0"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.secure = True

		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
	
		return api
	except:
		return None


def authenticate_test_app():
	try:
		consumer_key="RY4A89PLnuPKx8hIQRsGaQC0y"
		consumer_secret="iRO1tw96GuiCnb92WFg7Tmo60HgUgY7xHPLxsfMK6e4OpcqfPN"
		access_token="374363728-Vvr26iYvkW0HqLeDi4NMAe6ZmLwb8XCehaAEi7aH"
		access_token_secret="Q5qbv5S4ugYO7aiDI8D8IOnpIwU96r6aBZJdfLaxwgOI6"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.secure = True

		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
	
		return api
	except:
		return None



def authenticate_api_athlete():
	try:
		consumer_key="prpZDRZO2wMFw4l2Dy4tOoqWH"
		consumer_secret="O6P84x182pjZbIx4ENqFmCeeFUXu3x6u0enG3ItMNY8AYPkIEn"
		access_token="374363728-Vb3rn6HaVn0jlgHzTmiuU1HxxouDbp6JQtWFnm1V"
		access_token_secret="ZgloLWGdOfXADOYao2zLfJ2QxrAjiDzTygeBpoT2bdAPU"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.secure = True

		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
	
		return api
	except:
		return None


def authenticate_api_frank():
	try:
		consumer_key="IzxpLmPU7bcH6mkoEPhrDgCRz"
		consumer_secret="vqo6m3JU1TKRhSGwDHg8IxuvOZ4IGiiXdFxn8kgwuRTb5ijogZ"
		access_token="100311379-VJOuaxitBtDCq2WK11HXo3ROQSzDME7Ut1vL3AoI"
		access_token_secret="Ga3VCILMJkBd898Ewd3excvzicDPpepiRKvX0z9YMLM1q"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.secure = True

		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
	
		return api
	except:
		return None

def autheticate_api_frank_1():
	try:
		consumer_key="nM0kCPyrB06NA1EGH8kaQ"
		consumer_secret="hUaKXcXaVnnYQMpG46MkQaWEZW8uKCy8kU5piBY8R0"
		access_token="100311379-N9n7YrjaCYgdIBAe8d1jv90NkbcLL6TF9HQOZUJ5"
		access_token_secret="DiUsftqZiEXMZoNDSrxLzKdm9oCEcy1rSwMrXkHIQK7Nb"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.secure = True

		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)
	
		return api
	except:
		return None

def authenticate_test_stream():
	try:
		consumer_key="wwk0TZueG6EcXn5Qj72ZaeiaD"
		consumer_secret="AVRBLJu1al3XeQU7FC3yuAYNYiR3kSY8zkpxjiU3wQem75fdim"
		access_token="374363728-jTdIw2mWdJLXyD5oF3hkVnMXzyT4zlVckF1p5uTU"
		access_token_secret="iSmgkZFAiYrebXTu2JOoUYFnCtosrUCw8i6IcW19Awe7m"

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		#auth.secure = True

		auth.set_access_token(access_token, access_token_secret)

		#api = tweepy.API(auth)
	
		return auth
	except:
		return None

