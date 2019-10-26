#! /bin/sh

BERSERKERS_WEB='http://challenges.thecatch.cz/781473d072a8de7d454cddd463414034/'
cat hdr.py > out.py
IFS=';'
curl -b cook -c cook "${BERSERKERS_WEB}" 2> /dev/null \
| head -n1 | cut -c18- | while read data number ; do
	echo "${data}" | base64 -d | python build.py
	echo "convert("$(echo "${number}" | base64 -d)")"
done >> out.py

curl -b cook -c cook "${BERSERKERS_WEB}?answer=$(python out.py)" 2>/dev/null
