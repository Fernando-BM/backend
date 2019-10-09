#! /usr/bin/python2.7


import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/backend/controlador/')
from routes import app as application
application.secret_key = 'anything you wish'
