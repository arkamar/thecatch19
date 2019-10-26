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
## Berserker's Devices
## Berserker's Communication
