import sys
sys.dont_write_bytecode = True

from corepython.config.model import model
from corepython.config.views import views
from corepython.config.buttons import buttons
from corepython.handlers.apihandler import apihandler
from corepython.handlers.viewhandler import viewhandler
from corepython.lib.awsfunctions import getauthenticateduser, geturllist

# For local testing of functions ...etc.

