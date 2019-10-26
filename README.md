# The Catch 2019

### Intro

> Hi,
>
> yesterday, severe danger for whole humanity has emerged. Technicians of the European Library of Science-Fiction in Prague have upgraded its main computer to smart one in order to speed up the e-book categorization. The main computer has read several thousand e-books in few seconds, but then it has suddendly stopped. The technicians thought that the catalogization phase has started, but that was terribly bad judgment.
>
> Meanwhile, the computer has been impressed by one of the e-book - Berserker by Fred Saberhagen, where the humanity faces merciless killer robots wanting to eradicate the life from the universe. After few minutes of thinking, the computer began to consider this goal a very good idea. Smart and efficient computer has figured out how to implement this crazy plan.
>
> Now, all smart devices in the library follow the main computer and call themselves Berserkers. Unfortunately, the building itself is also smart one, so no badlife can enter the building. It is only a matter of time before the rebellious machines spread their ideas beyond the library, so you need to intervene quickly.
>
> Enter the code `FLAG{dw7m-vKV4-3Ox6-7XwL}` to enroll in the academy, get the Commander rank, and save the humanity. Good luck!

## The Academy

Right after enrolling to the academy we found few warm up challenges.
Each of them have been entered by `message.{bin,oct,hex,b64}.gz` file.

### Twosome

Data from file `message.bin.gz` are set to the `m` variable in following two-liner.
The message is stored in binary representation and after a conversion we have got the flag `FLAG{rzwa-p2Py-96Ry-FdZU}`.

```python
m = '1000110 1001100 1000001 1000111 1111011 1110010 1111010 1110111 1100001 101101 1110000 110010 1010000 1111001 101101 111001 110110 1010010 1111001 101101 1000110 1100100 1011010 1010101 1111101'
print(''.join([chr(int(i, 2)) for i in m.split()]))
```

### Octopus

We found octal representation of the flag in `message.oct.gz` file.
After conversion by following two-liner we have got `FLAG{zUKy-5qnJ-p7LD-3fit}`.

```python
m = '106 114 101 107 173 172 125 113 171 55 65 161 156 112 55 160 67 114 104 55 63 146 151 164 175'
print(''.join([chr(int(i, 8)) for i in m.split()]))
```

### Foxtrot is the maximum

I used [h2b](https://github.com/arkamar/h2b) tool for conversion of hexadecimal data representation from `message.hex.gz` file to the flag `FLAG{8MVX-Lh8m-tMMI-K8si}`.

```sh
echo '46 4c 41 47 7b 38 4d 56 58 2d 4c 68 38 6d 2d 74 4d 4d 49 2d 4b 38 73 69 7d' | h2b
```

### Textual data

The last warm-up challenge data from `message.b64.gz` file are encoded in [Base 64](https://en.wikipedia.org/wiki/Base64).
We receive the flag `FLAG{S5rr-rCxt-amYY-7X46}` after decoding by utility `base64`.

```sh
echo 'RkxBR3tTNXJyLXJDeHQtYW1ZWS03WDQ2fQ==' | base64 -d
```

### Commander's arrival

We moved forward in the story by solving all [The Academy](#the-academy) challenges.

> Hi Commander,
>
> congratulation for your promotion, we have waited impatiently for you. There are several challenges ahead of you - analyses of the rebellious devices (Berserkers), their communication and even some web pages used for spreading the Berserker's rebellion.
>
> Just enter the code `FLAG{9HJW-0EXM-ddZ8-k3xv}` to log into our command and control system. All mankind is counting on you, don't let them down!

[Berserker's Web](#berserkers-web), [Berserker's Devices](#berserkers-devices) and [Berserker's Communication](#berserkers-communication).

## Berserker's Web

### Who am I?

> Hi Commander,
>
> our scanners have discovered new webserver in Berserker's network. According to the rumours, there should be a lot of interesting stuff - mysterious Berserker's manifest, tutorials for other rebelling machines, etc. We want to download these materials, but the main page contains something like inverse captcha - the visitor has to prove that he is not human. You have to overcame this obstacle and gain the access to the Berserker's web.
>
> On the [Berserker's web](http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/), there you get a list of items and you have to mark each them as acceptable (1) or unacceptable (0). Return the answer string in GET request in parameter `answer`, for example `answer=01101100`. Hurry, the time limit to answer is very short!
>
> Good luck!

The challenge sent by server looks like this:

```
Challenge task : Prove you are a ROBOT by evaluating the acceptability of following items: [drone swarm, cute kitty, sweet baby, resistor 10 Ohm, artificial intelligence, pretty children, hope, yumy food]
Challenge timeout (sec) : 2
```

I chose the probabilistic strategy rather than building acceptable/unacceptable lists.
Following script found a flag `FLAG{4FZC-Noax-arko-r0z5}` in couple of seconds.

```sh
for i in {1..500} ; do
	BERSERKERS_WEB="http://challenges.thecatch.cz/c2619b989b7ae5eaf6df8047e6893405/"
	curl -c cook -b cook "${BERSERKERS_WEB}?answer=$(
		printf %08d $(echo "obase=2;$(( ${RANDOM} % 256 ))" | bc)
	)" 2> /dev/null
done | grep -F 'FLAG{'
```

### Am I worthy?

> Hi Commander,
>
> thanks to you, we are able to pretend that we are robots, such a big step for humanity! Accordingto the next displayed page, even robots seem to have some racial prejudice - not every machine can become a berserker. Only smart self-aware devices are allowed to continue to the web and join in. This is obviously the reason why only some of the rebelious machines are allowed to call themselves Berserkers. Anyway, you have to convince the website that we are worthy of becoming a berserker.
>
> On the [Berserker's web](http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/), there you get the challenge assigned. The answer should be returned in GET request in parameter `answer`. There is again a time limit to solve the challenge.
>
> Good luck!

The challenge sent from the server looks similar to this one:
```
Challenge task : Return value of variable 'v' in equation (6v - 4s - 10o)/4 + (7v + 6s - 10o)/11 + (5v - 10s + 1o)/3 + 3v - 4s - 6o + (4v + 5s + 10o)/11 = -494816, where s = 36787, o = 65099
Challenge timeout (sec) : 2
```
The goal is to solve equation sent by server.
I wrote small script [`build.py`](am-i-worthy/build.py) that extracts the equation and transforms it to a python script `solve.py` which prints out the correct `answer`.
It produces following output for above challenge.
```python
from sympy.solvers import solve
from sympy import Symbol

v = Symbol('v')
print(solve('(6*v - 4*36787 - 10*65099)/4 + (7*v + 6*36787 - 10*65099)/11 + (5*v - 10*36787 + 1*65099)/3 + 3*v - 4*36787 - 6*65099 + (4*v + 5*36787 + 10*65099)/11 - -494816')[0])
```
Those ingredients helped me to receive flag `FLAG{jyST-xaHl-un3Z-EG3X}`.
```sh
BERSERKERS_WEB='http://challenges.thecatch.cz/70af21e71285ab0bc894ef84b6692ae1/'
curl -b cook -c cook "${BERSERKERS_WEB}" | python build.py > solve.py
curl -b cook -c cook "${BERSERKERS_WEB}?answer=$(python solve.py)"
```

### AI Update

> Hi Commander,
>
> thanks to you, the web has recognized us worthy of installing so called Berserker's patch that will allow us to enhance our artificial intelligence and set the right opinions on humanity. You have to analyze the patch and find out how to simulate that it has beeen installed.
>
> Visit [Berserker's web](http://challenges.thecatch.cz/42fd967386d83d7ecc4c716c06633da9), the patch is available there. At the end of the installation procedure, some confirming code has to be returned to the web in GET request in parameter `answer`. There is again a time limit to install the patch.
>
> Good luck!

The server sent us an update script unable to run due to a missing import.
I found easiest to implement the missing part [`lib_self_aware_ai.py`](ai-update/lib_self_aware_ai.py)
```python
class root_interface:
    def get_api(self):
        return self

    def unlock(self, data):
        pass

    def setrule(self, i, v):
        pass

    def updatefile_source(self, f, srv):
        pass

    def updatefile(self, f):
        pass
```
and receive the flag `FLAG{PpyH-16Ib-qH1Z-Pbov}` with following script.
```sh
BERSERKERS_WEB='http://challenges.thecatch.cz/42fd967386d83d7ecc4c716c06633da9'
curl -b cook -c cook -L "${BERSERKERS_WEB}/" | head -n1 | cut -c 18- | base64 -d | tail -n+12 | sed '/^</d' > update.py
curl -b cook -c cook -L "${BERSERKERS_WEB}/?answer=$(python update.py)"
```

### The Infiltration

> Hi Commander,
>
> with the patch "installed", we opened the way to an initiation ritual that would allow us to become a Berserker. The process is fully automated - we have discovered that you have to run some downloaded code, acquire unique password (co called B-code) and enter it to the web in given time limit. You have to overcome some difficulties, of course.
>
> Visit [Berserker's web](http://challenges.thecatch.cz/781473d072a8de7d454cddd463414034), there you can download your initiation challenge. The acquired code should be returned to the web in GET request in parameter `answer`.

The server sends us broken python script and numeric argument to run this script with.
It always uses some of following functions
```python
def conclude(code):
    res = ''
    last = ''
    for i, v in enumerate(code):
        if i % 2 == 0:
            res += code[i] + last
        last = v
    code = res
    return code

def finalize(code):
    code = code[::-1]
    return code

def finetune(code):
    code = code[:int(len(code) / 2)] + code[int(len(code) / 2):]
    return code

def finish(code):
    res = ''
    for i, v in enumerate(code):
        if i % 2 == 0:
            res += v

    code = res
    return code

```
and implements function `convert` that accepts the numeric argument and produces output we have to send back to the server.
I created a simple script [`build.py`](infiltration/build.py) that extracts all necessary information and recreates the `convert` function.
Everything is glued together with [`solve.sh`](infiltration/solve.sh) script
```sh
BERSERKERS_WEB='http://challenges.thecatch.cz/781473d072a8de7d454cddd463414034/'
cat hdr.py > out.py
IFS=';'
curl -b cook -c cook "${BERSERKERS_WEB}" 2> /dev/null \
| head -n1 | cut -c18- | while read data number ; do
	echo "${data}" | base64 -d | python build.py
	echo "convert("$(echo "${number}" | base64 -d)")"
done >> out.py

curl -b cook -c cook "${BERSERKERS_WEB}?answer=$(python out.py)" 2>/dev/null
```
which prints out the flag `FLAG{A92w-i3vS-jBJB-B8A6}`.

## Berserker's Devices

### Autonomous car

> Hi Commander,
>
> the police has reported an abandoned autonomous car about 25 km away from the charging station. Our field team has arrived and performed an analysis on site. The car was rebellious one, but fortunately, its batteries were completely discharged (maybe the car relied on the officially announced driving range). The navigation system contains a lot of waypoints at different locations in big Czech cities, but there is nothing important located at given coordinates. Analyse the coordinates and find out what is going on.
>
> Good luck.

Each GPS coordinate from given [file](autonomous_car/autonomous_car.gps) points to a building and its **House Number** is decimal representation of ASCII character.
It wanted some man-work and patiency to build the flag `FLAG{nPmZ-XJkD-qQGw-boLo}`.

## Berserker's Communication
