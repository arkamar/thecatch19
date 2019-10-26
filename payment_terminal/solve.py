#! /usr/bin/python

key = '0804545A1B18360300040203641B256C770272010355'
xlat = "dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87"

seed = (ord(key[0]) - 0x30) * 10 + ord(key[1]) - 0x30

if seed > 15 or not ord(key[0]) or not ord(key[1]):
    print("Shit")

out = ''
val = 0
for i in range(2, len(key)):
    if i != 2 and not (i & 1):
        out += chr(val ^ ord(xlat[seed]))
        seed += 1
        seed %= len(xlat)
        val = 0
    val *= 16

    if key[i] in "0123456789":
        val += ord(key[i]) - 0x30
        continue

    if ord(key[i]) >= 0x41 and ord(key[i]) <= 0x46:
        val += ord(key[i]) - 0x41 + 0x0a
        continue

    if len(key) != i:
        break


print(out)
