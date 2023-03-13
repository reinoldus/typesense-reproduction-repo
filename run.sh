#!/bin/bash

docker network create typesense-test-network

echo "RUNNING DOCKER CONTAINER"
docker run --network typesense-test-network --rm --name test-typesense -d typesense/typesense:0.24.0 /opt/typesense-server --data-dir / --api-key=test --enable-cors &> typesense-start.logs



echo "BUILDING TEST IMAGE"
docker build -t test-typesense-python:latest ./  &> test-container-build-log.logs

echo "====== TEST OUTPUT START"
docker run --network typesense-test-network --rm --name test-typesense-container test-typesense-python
echo "====== OUTPUT END"

docker rm -f test-typesense
docker image rm test-typesense-python

docker network rm typesense-test-network