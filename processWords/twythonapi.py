from twython import Twython

consumer_key="hhYq78kZ6VkAp4Q4pXzuKCOkA"
consumer_secret="A468W3FnFd9WcL2PXYeRO0iLWnu90761HkKHijXRXqmgtR1bpk"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="374363728-BCe1rusHWiVPBHDCQ5RoketbfaNePuHXTeJja7W6"
access_token_secret="cMyNaQwVzxtXKqSG0jjlI1H6avEoMbvZ36pB7Zr5dPEN0"

twitter = Twython(consumer_key,
                      consumer_secret,
                      access_token,
                      access_token_secret)
followers = twitter.get_followers_ids(screen_name = "QuincyAcy")

#followers = twitter.get_followers_list(screen_name = "QuincyAcy")

#for follower_id in followers['users']:
#    print("User with ID is following ryanmcgrath", follower_id['screen_name'])

for follower_id in followers['ids']:
    print("User with ID is following ryanmcgrath", follower_id)
