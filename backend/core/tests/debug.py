import sys
sys.dont_write_bytecode = True

from core.config.model import model
from core.config.views import views
from core.config.function import functions
from core.handlers.apihandler import apihandler
from core.handlers.viewhandler import viewhandler
from core.lib.awsfunctions import getauthenticateduser, geturllist

# For local testing of functions ...etc.

