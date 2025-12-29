#!/bin/bash

cd corego/webhandler

GOOS=linux GOARCH=amd64 go build -o bootstrap main.go
chmod +x bootstrap
zip -j bootstrap.zip bootstrap