#! /usr/bin/env python
"""
Posts Twits using Python
Needs a vars.cfg file with some Twitter API info
Uses tweepy library
"""

__author__ = "Aaron Castro"
__author_email__ = "aaron.castro.sanchez@outlook.com"
__copyright__ = "Aaron Castro"
__license__ = "MIT"


import tweepy, argparse, sys, configparser

def main():
    config = configparser.ConfigParser()
    config.read("vars.cfg")
    consumer_secret = config.get("api_vars", "consumer_secret").strip("\"")
    consumer_key = config.get("api_vars", "consumer_key").strip("\"")
    access_token = config.get("api_vars", "access_token").strip("\"")
    access_token_secret = config.get("api_vars", "access_token_secret").strip("\"")
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    api.update_status("Hello world!")

if __name__ == "__main__":
	main()
