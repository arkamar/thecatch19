#! /bin/sh

BERSERKERS_WEB='http://challenges.thecatch.cz/42fd967386d83d7ecc4c716c06633da9'
curl -b cook -c cook -L "${BERSERKERS_WEB}/" | head -n1 | cut -c 18- | base64 -d | tail -n+12 | sed '/^</d' > update.py
curl -b cook -c cook -L "${BERSERKERS_WEB}/?answer=$(python update.py)"
