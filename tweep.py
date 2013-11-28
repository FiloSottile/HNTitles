#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import random
import time
import os

random.seed()

import hngen

CONSUMER_KEY = 'l8EfO9PGlgTn5LqQCR0Ug'
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = '2220426313-DS56JVoKYuJDWY8l9UuPdUBNEDBtnPIzQsfJs4s'
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print('')
    status = hngen.get_sentence()
    if status.count('"') % 2 != 0: status = status.replace('"', '')
    if status.count('(') != status.count(')'):
        status = status.replace('(', '').replace(')', '')
    print(status)
    r = random.random()
    if r < 0.2:
        print('Draw a {:f}, publishing...'.format(r))
        api.update_status(status)
    else:
        print('Draw a {:f}, skipping.'.format(r))
    time.sleep(3600)
