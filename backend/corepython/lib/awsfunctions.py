import json
import requests
from jose import jwk, jwt
from jose.utils import base64url_decode

def getauthenticateduser(event):
    try:
        token = event['headers']['Authorization']
        accesstoken = token.split('Bearer ')[1]
        decode = jwt.get_unverified_header(accesstoken)

        jwksurl = 'https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_j2ARZDsZL/.well-known/jwks.json'
        jwks = requests.get(jwksurl).json()

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
            return False, 'error - Wrong token passed to backend'
    except Exception as e:
        return False, f"error - {str(e)}"


def geturllist(event):
    path = event.get("path") or {}
    urllist = path.split('/')
    if urllist[0] == '':
        urllist.pop(0)
    if urllist[0] == 'dev':
        urllist.pop(0)
    return urllist

