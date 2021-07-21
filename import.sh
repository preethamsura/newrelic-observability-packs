#!/usr/bin/env bash

accountId=$(grep -E '^accountId' ./importer-config.sh | sed s/.*=//)

apiKey=$(grep -E '^apiKey' ./importer-config.sh | sed s/.*=//)

PACK=$1

while (( "$#" )); do
  case "$2" in
    -a|--copy)
      COPY_FLAG=$3
      echo 'Creating copies from copy json at:' $3
      python3 utils/create_copies.py $3
      echo 'Copy creation was successful'
      shift
      ;;
    -*|--*=) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      exit 1
      ;;
    *) # preserve positional arguments
      PARAMS="$PARAMS $1"
      shift
      ;;
  esac
done

docker-compose run importer -- --accountId $accountId --nrApiKey $apiKey $PACK

