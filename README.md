# Docker to host proxy

## What?

Simple TCP proxy that listens to a container port (LISTEN) and talks a host port (TALK).

## Usage

The environment variable `PROXY_PASS` follows the same port syntax as docker-compose specification `HOST:CONTAINER`. For example `PROXY_PASS=4000:3000` would pass requests from docker network port 3000 to the docker host network 4000.
