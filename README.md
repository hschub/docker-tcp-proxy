# Docker to host proxy

## What?

Simple TCP proxy that listens to a container port (LISTEN) and talks a host port (TALK).

## Usage

`LISTEN=3000` Listens to port 3000 on the docker network
`TALK=4000` Passes requests from docker-container port 3000 to host machine 4000
