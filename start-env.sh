#!/bin/bash

unset INSTANCE_CONNECTION_NAME
unset GAE_APPLICATION
unset GOOGLE_APPLICATION_CREDENTIALS
unset GS_BUCKET_NAME
unset PGHOST
unset PGPORT
unset PGDATABASE
unset PGUSER
unset PGPASSWORD

# Add environment variables from .env to environment
echo "Loading environment variables..."

set -a
source .env-common
set +a

if [ "$1" = "gae" ]; then

set -a
source .env
set +a

fi
