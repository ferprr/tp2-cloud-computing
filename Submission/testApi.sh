#!/bin/bash
curl --location 'http://127.0.0.1:32192/api/recommend' \
--header 'Content-Type: application/json' \
--data '{
    "songs": ["Billie Jean"]
}'