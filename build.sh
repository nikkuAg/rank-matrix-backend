#!/bin/bash

# Build the container from the Django folder and tag it
TIMESTAMP=$(date +"%s")

docker build \
    --tag rank-matrix-backend:${TIMESTAMP} \
    --tag rank-matrix-backend:latest \
    .
