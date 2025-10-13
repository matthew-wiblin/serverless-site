package main

import (
	"encoding/json"
	"fmt"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

func main() {
	lambda.Start(handler)
}

func handler(request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {

	fmt.Println("func handler ran")

	body, _ := json.Marshal(map[string]string{
		"message": "Go function ran",
	})

	response := events.APIGatewayProxyResponse{
		StatusCode: 200,
		Headers:    map[string]string{"Access-Control-Allow-Origin": "*"},
		Body:       string(body),
	}

	return response, nil
}
