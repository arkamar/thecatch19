#! /bin/sh

BERSERKERS_WEB='http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/'
curl -b cook -c cook "${BERSERKERS_WEB}" | python build.py > solve.py
curl -b cook -c cook "${BERSERKERS_WEB}?answer=$(python solve.py)"
