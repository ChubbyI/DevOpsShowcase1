#!/usr/bin/env bash

# Set project name
project_name="your_project_name"

current_branch=$(git branch --show-current)
date_now=$(date '+%Y%m%d')
version="v1"

# Build Docker Image
docker build -t "chubbyi/${project_name}-${current_branch}-${date_now}:${version}" . 

# Push to Docker Hub
docker push "chubbyi/${project_name}-${current_branch}-${date_now}:${version}"


# Ensure your workstation has the proper permision for the docker account you are trying to push to and change the username from "chubbyi" to your user name in the build and push steps. 