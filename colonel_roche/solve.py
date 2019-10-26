#! /usr/bin/python

msg = '463216327617246f67406f1266075ec622606c6671765537066636596e621e64e622c2b006066961c66e621f067676e77c6e665167a462c4b50477433617754222d7043542885747df6dd575970417d435223000'

def key_idx(key):
    l = [ (i, v) for i, v in enumerate(key) ]
    l.sort(key = lambda a: a[1])
    o = [None]*len(l)
    for i, v in enumerate(l):
        o[v[0]] = i + 1
    return o

def decrypt(msg, key):
     ki = key_idx(key)
     s = 0
     t = [None] * len(ki)
     for i, v in enumerate(ki):
         t[i] = msg[s: s + v]
         s += v
     o = ''
     j = 0
     while s:
         for i in t:
             if j < len(i):
                 o += i[j]
                 s -= 1
         j += 1
     return o

for i in range(0, len(msg), 21):
    plain = decrypt(msg[i:], 'monday')
    print(plain)
