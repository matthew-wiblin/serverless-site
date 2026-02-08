import requests
from jose import jwk, jwt

from corepython.config.constants import JWKSURL

class Event:
    def __init__(self, event):
        self.event = event
        self.isloggedin, self.username = self._getauthenticateduser()
        self.urllist = self._geturllist()

    def _getauthenticateduser(self):
        try:
            token = self.event['headers']['Authorization']
            accesstoken = token.split('Bearer ')[1]
            decode = jwt.get_unverified_header(accesstoken)

            jwks = requests.get(JWKSURL).json()

            kid = decode['kid']
            matchingkey = next(key for key in jwks['keys'] if key['kid'] == kid)
            key = jwk.construct(matchingkey)

            decodedpayload = jwt.decode(
                accesstoken,
                key,
                algorithms=['RS256']
            )

            if decodedpayload['token_use'] == 'access':
                return True, decodedpayload['username']
            else:
                return False, None
        except Exception as e:
            return False, None

    def _geturllist(self):
        path = self.event.get("path") or {}
        urllist = path.split('/')
        if urllist[0] == '':
            urllist.pop(0)
        if urllist[0] == 'dev':
            urllist.pop(0)
        return urllist
