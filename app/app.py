import tweepy
import dog
from postDog import postDog
from config import data

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(data["OAUTH_HANDLER_1"], data["OAUTH_HANDLER_2"])
    auth.set_access_token(data["API_KEY_1"], data["API_KEY_2"])

    api = tweepy.API(auth)

    dogPic = dog.getDog(filename='assets/doggy')

    postDog(api)