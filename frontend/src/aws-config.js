// aws-config.js
import { Amplify } from 'aws-amplify';

Amplify.configure({
  Auth: {
    Cognito: {
      region: 'eu-west-2',
      userPoolId: 'eu-west-2_j2ARZDsZL',
      userPoolClientId: '6q9c36eaqodo1e612mel9rf3ho',
      signUpVerificationMethod: "code",
      userAttributes: {
        email: {
          required: true,
        },
      },
    }
  },
});
