import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import { AuthProvider } from "react-oidc-context";

const cognitoAuthConfig = {
  authority: "https://cognito-idp.eu-west-2.amazonaws.com/eu-west-2_j2ARZDsZL",
  client_id: "6q9c36eaqodo1e612mel9rf3ho",
  redirect_uri: "http://localhost:5173",
  response_type: "code", // edit this to not include ?code= after logging in ???
  scope: "email openid phone",
};

// Below is the default cognito route
// redirect_uri: "https://d84l1y8p4kdic.cloudfront.net",

const root = ReactDOM.createRoot(document.getElementById("root"));

// wrap the application with AuthProvider
root.render(
  <React.StrictMode>
    <AuthProvider {...cognitoAuthConfig}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </AuthProvider>
  </React.StrictMode>
);
