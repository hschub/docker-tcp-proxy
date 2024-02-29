#!/usr/bin/env python3

import logging
import os
import sys

from dns.resolver import Resolver

logging.root.setLevel(logging.INFO)

CONTAINER = os.environ["CONTAINER"]
HOST = os.environ["HOST"]
NAMESERVERS = os.environ["NAMESERVERS"].split()
resolver = Resolver()
resolver.nameservers = NAMESERVERS
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
    listen=f":{CONTAINER}",
    talk=f"host.docker.internal:{HOST}",
)

# Write template to haproxy's cfg file
with open("/usr/local/etc/haproxy/haproxy.cfg", "w") as cfg:
    cfg.write(config)

logging.info(f"Proxying container:{CONTAINER} TO host:{HOST}")
os.execv(sys.argv[1], sys.argv[1:])
