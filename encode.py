#!/usr/bin/env python

import state
from common import checksum

SHORT_TIME = 550
LONG_TIME = 1550
TIME_4000 = 4350
TIME_5000 = 5150

INTRO = [TIME_4000,TIME_4000]
MIDDLE = [TIME_5000, TIME_4000, TIME_4000]

def encode(state):
    d = state.data()
    chk = checksum(d)
    d.extend(chk)

    out = encodeData(d)
    return out

def encodeData(data):
    r = INTRO
    for d in data:
        r.append(SHORT_TIME)
        if d == True:
            r.append(LONG_TIME)
        else:
            r.append(SHORT_TIME)
    r.append(SHORT_TIME)

    data.invert()
    r.extend(MIDDLE)
    for d in data:
        r.append(SHORT_TIME)
        if d == True:
            r.append(LONG_TIME)
        else:
            r.append(SHORT_TIME)

    r.append(SHORT_TIME)

    return r

def main():
    s = state.StateOn(
        state.Mode.COOL,
        23,
        state.FanSpeed.MIN
    )
    data = encode(s)

    pulse = True
    for d in data:
        if pulse:
            print("pulse: {}".format(d))
        else:
            print("space: {}".format(d))
        pulse = not pulse

if __name__ == '__main__':
    main()
