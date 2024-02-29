ARG ARCH=
FROM ${ARCH}haproxy:1.9-alpine

ENTRYPOINT ["/magic-entrypoint", "/docker-entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

RUN apk add --no-cache python3 cmd:pip3 &&\
    pip3 install --no-cache-dir dnspython

COPY magic-entrypoint.py /magic-entrypoint

ENV DEFAULT_TIMEOUT=30s

ENV NAMESERVERS="208.67.222.222 8.8.8.8 208.67.220.220 8.8.4.4" \
    LISTEN=:100 \
    PRE_RESOLVE=0 \
    TALK=talk:100 \
    TIMEOUT_CLIENT=$DEFAULT_TIMEOUT \
    TIMEOUT_CLIENT_FIN=$DEFAULT_TIMEOUT \
    TIMEOUT_CONNECT=$DEFAULT_TIMEOUT \
    TIMEOUT_SERVER=$DEFAULT_TIMEOUT \
    TIMEOUT_SERVER_FIN=$DEFAULT_TIMEOUT \
    TIMEOUT_TUNNEL=$DEFAULT_TIMEOUT \
    UDP=0 \
    VERBOSE=0
