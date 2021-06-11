package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	port := "8080"
	if v := os.Getenv("PORT"); v != "" {
		port = v
	}
	http.HandleFunc("/", handler)

	log.Printf("starting server on port :%s", port)
	err := http.ListenAndServe(":"+port, nil)
	log.Fatalf("http listen error: %v", err)
}

func handler(w http.ResponseWriter, req *http.Request) {
	if req.Method != http.MethodPost {
		w.WriteHeader(http.StatusMethodNotAllowed)
		fmt.Fprint(w, "only POST method supported")
		return
	}

	defer req.Body.Close()

	/*
		You should return a json response with the following format:
		{
			"username": "Kang",        //The registered username
			"flag": "jplOsDIaFLhcMRlS" //The 16-word random generated string
		}
	*/
	resp := "This is your go microservice."
	fmt.Fprint(w, resp)
}
