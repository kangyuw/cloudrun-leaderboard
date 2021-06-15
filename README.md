# RPT and GCP event Leaderboard

## Techstack

Backend: Python-Django 3.2

Frontend: Bootstrap5

Database: Postgresql

Google Cloud services: Cloud Run, Cloud SQL, Artifact Registry
## Deploy

It would take about 5-10 minutes to deploy the project on gcloud.

1. Follow [the instruction](https://cloud.google.com/python/django/run) to set up new project, Cloud Run, Cloud SQL and Artifact Registry instance.
2. Pull/Clone the latest version from [GitLab Repo](https://gitlab.com/kangyuw/cloudrun-leaderboard)
3. Run ```bash build.sh``` in gcloud console terminal to deploy the container as per ```cloudmigrate.yaml``` structured.
4. Run ```bash run.sh``` in gcloud console terminal to create and deploy the project on the Cloud Run.

## Disclaimer

There are some hard-coded part scatter through following files:

* ```cloudmigrate.yaml```: the ```substitutions``` section
* ```build.sh```
* ```run.sh```