#! /usr/bin/python

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

