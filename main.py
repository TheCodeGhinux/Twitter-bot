import tweepy as tp

# Authenticate to Twitter
auth = tp.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tp.API(auth)

# Create a tweet
api.update_status("Hello, This is {The Code Ghinux}")
