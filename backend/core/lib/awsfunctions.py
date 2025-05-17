import json
import requests
from jose import jwk, jwt
from jose.utils import base64url_decode

def isauthenticated(token):
    try:
        accesstoken = token.split('Bearer ')[1]
        decode = jwt.get_unverified_header(accesstoken)

        jwks_url = 'https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_j2ARZDsZL/.well-known/jwks.json'
        jwks = requests.get(jwks_url).json()

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

