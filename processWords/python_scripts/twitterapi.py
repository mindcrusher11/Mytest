import twitter

consumer_key="hhYq78kZ6VkAp4Q4pXzuKCOkA"
consumer_secret="A468W3FnFd9WcL2PXYeRO0iLWnu90761HkKHijXRXqmgtR1bpk"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="374363728-BCe1rusHWiVPBHDCQ5RoketbfaNePuHXTeJja7W6"
access_token_secret="cMyNaQwVzxtXKqSG0jjlI1H6avEoMbvZ36pB7Zr5dPEN0"

api = twitter.Api(consumer_key,
                      consumer_secret,
                      access_token,
                      access_token_secret)

#statuses = api.GetUserTimeline(screen_name="QuincyAcy")
statuses = api.GetUserTimeline(screen_name='Akil Mitchell')
print [s.text for s in statuses]


