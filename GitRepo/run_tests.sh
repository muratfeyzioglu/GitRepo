#!/bin/bash

# Check if Docker is installed
if ! command -v docker &> /dev/null
then
    echo "Error: Docker is not installed. Please install Docker before running the tests."
    exit 1
fi

# Build the Docker image
docker build -t pytest-weld .

# Run the Docker container and execute tests
docker run -v $(pwd):/app pytest-weld /bin/bash -c "pytest testCases/ --junitxml=/app/test_results/results.xml"

# Copy the results from the container to the host machine
docker cp $(docker ps -q -n=1):/app/test_results/results.xml ./test_results/results.xml
