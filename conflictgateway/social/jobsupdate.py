#!/usr/bin/env python

from twython import Twython
import random

APP_KEY = 'APP KEY'  # Customer Key here
APP_SECRET = 'APP SECRET'  # Customer secret here
OAUTH_TOKEN = 'OAUTH TOKEN'  # Access Token here
OAUTH_TOKEN_SECRET = 'OAUTH TOKEN SECRET'  # Access Token Secret here

jobsnumber = random.randint(50, 100)

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.update_status(status="Weekly jobs update: " + str(jobsnumber) + " Mediation & Conflict Resolution jobs & scholarships added... http://www.conflictgateway.com/jobs")