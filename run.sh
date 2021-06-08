#!/bin/bash

# gcloud run deploy polls-service \
#     --platform managed \
#     --region REGION \
#     --image gcr.io/PROJECT_ID/polls-service \
#     --add-cloudsql-instances PROJECT_ID:REGION:INSTANCE_NAME \
#     --allow-unauthenticated


gcloud run deploy leaderboard-service \
    --platform managed \
    --region us-east1 \
    --image gcr.io/leaderboard-315819/leaderboard-service \
    --add-cloudsql-instances leaderboard-315819:us-east1:leaderboard \
    --allow-unauthenticated