import json
import requests
import jwt
from jwt.algorithms import RSAAlgorithm


def is_authenticated(token):
    try:
        accesstoken = token.split('Bearer ')[1]
        decode = jwt.get_unverified_header(accesstoken)

        jwks_url = 'https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_j2ARZDsZL/.well-known/jwks.json'
        jwks = requests.get(jwks_url).json()

        kid = decode['kid']
        matchingkey = next(key for key in jwks['keys'] if key['kid'] == kid)

        publickey = RSAAlgorithm.from_jwk(json.dumps(matchingkey))

        decodedpayload = jwt.decode(
            accesstoken,
            publickey,
            algorithms=['RS256']
        )

        if decodedpayload['token_use'] == 'access':
            return decodedpayload['username']
        else:
            return 'error - Wrong token passed to backend'
    except Exception as e:
        return f"error - {str(e)}"

