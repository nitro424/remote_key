#!/bin/bash
docker run -it --name=remote_key -p 8000:8000 --rm -e CRYPT_STORE_PATH=/remote_key/store -e DAEMON=False remote_key