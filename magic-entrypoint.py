#!/usr/bin/env python3

import logging
import os
import sys

logging.root.setLevel(logging.INFO)

HOST_PORT,CONTAINER_PORT = os.environ["PROXY_PASS"].split(':')
TEMPLATE = """
backend talk_0
    server stupid_0 {talk}

frontend listen_0
    bind {listen}
    default_backend talk_0
"""
config = """
global
    log stdout format raw daemon

defaults
    log global
    mode tcp
    timeout client "$TIMEOUT_CLIENT"
    timeout client-fin "$TIMEOUT_CLIENT_FIN"
    timeout connect "$TIMEOUT_CONNECT"
    timeout server "$TIMEOUT_SERVER"
    timeout server-fin "$TIMEOUT_SERVER_FIN"
    timeout tunnel "$TIMEOUT_TUNNEL"
"""

# Render template
config += TEMPLATE.format(
    listen=f":{CONTAINER_PORT}",
    talk=f"host.docker.internal:{HOST_PORT}",
)

# Write template to haproxy's cfg file
with open("/usr/local/etc/haproxy/haproxy.cfg", "w") as cfg:
    cfg.write(config)

logging.info(f"Proxying container:{CONTAINER_PORT} TO host:{HOST_PORT}")
os.execv(sys.argv[1], sys.argv[1:])
