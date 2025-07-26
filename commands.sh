# Prerequisite commands to run before using the compose file:
#!/bin/bash
docker network create infra-ai-net
mkdir -p /root/docker-storage/infra-proxy/data
mkdir -p /root/docker-storage/infra-proxy/letsencrypt
mkdir -p /root/docker-storage/portainer
mkdir -p /root/docker-storage/workflow
mkdir -p /opt/custom-certificates
mkdir -p /root/docker-storage/pgdata
mkdir -p /root/docker-storage/pgdata-memory
mkdir -p /root/docker-storage/qdrant-data
mkdir -p /root/docker-storage/open-webui
mkdir -p /root/docker-static/infra-certs/ca-certificates.crt
chmod -R 0777 /root/docker-storage/