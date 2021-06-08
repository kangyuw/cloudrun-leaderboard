#!/bin/bash

# gcloud builds submit --config cloudmigrate.yaml \
#     --substitutions _INSTANCE_NAME=INSTANCE_NAME,_REGION=REGION


gcloud builds submit --config cloudmigrate.yaml \
    --substitutions _INSTANCE_NAME=leaderboard,_REGION=us-east1