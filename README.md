# lennoxir
Lennox mini-split heatpump infrared library in Python

This project aim to control a Lennox mini-split heatpump with a Raspberry Pi and a small infrared circuit connected to the GPIO.

## Hardware
To decode the initial Lennox protocol and to send the infrared signal, I've built a small electronic circuitusing the project
from [bbtinkerer](https://www.instructables.com/member/bbtinkerer/) at https://www.instructables.com/id/Raspberry-Pi-Zero-Universal-Remote/

## Protocol
All the informations from the remote control are send to the heatpump unit everytime a button is pressed on the remote control:
power, fan speed, mode, temperature, program. These informations are encoded in a simple protocol with a checksum.

Pulse and space represent the infrared light ON and OFF during an amount of time in microseconds.

```MESSAGE: INTRODUCTION ENCODEDDATA MIDDLE REVERSEDENCODEDDATA```

The message consist of an introduction, the data, a middle signal and the data reversed.

```INTRODUCTION: pulse 4350 space 4350```

```
1        2        3        4        5       
1      8 9     16 17    24 25    32 33    40
00000000 00000000 00000000 00000000 00000000
10100001 P0FFFMMM 0100TTTT 11111111 11111111

Temperature
17
xxxxxxxx xxxxxxxx xxxx0000 xxxxxxxx xxxxxxxx
18
xxxxxxxx xxxxxxxx xxxx0001 xxxxxxxx xxxxxxxx
19
xxxxxxxx xxxxxxxx xxxx0010 xxxxxxxx xxxxxxxx
20
xxxxxxxx xxxxxxxx xxxx0011 xxxxxxxx xxxxxxxx
21
xxxxxxxx xxxxxxxx xxxx0100 xxxxxxxx xxxxxxxx
22
xxxxxxxx xxxxxxxx xxxx0101 xxxxxxxx xxxxxxxx
23
xxxxxxxx xxxxxxxx xxxx0110 xxxxxxxx xxxxxxxx
24
xxxxxxxx xxxxxxxx xxxx0111 xxxxxxxx xxxxxxxx
25
xxxxxxxx xxxxxxxx xxxx1000 xxxxxxxx xxxxxxxx
26
xxxxxxxx xxxxxxxx xxxx1001 xxxxxxxx xxxxxxxx
27
xxxxxxxx xxxxxxxx xxxx1010 xxxxxxxx xxxxxxxx
28
xxxxxxxx xxxxxxxx xxxx1011 xxxxxxxx xxxxxxxx
29
xxxxxxxx xxxxxxxx xxxx1100 xxxxxxxx xxxxxxxx
30
xxxxxxxx xxxxxxxx xxxx1101 xxxxxxxx xxxxxxxx
OFF/FAN
xxxxxxxx xxxxxxxx xxxx1110 xxxxxxxx xxxxxxxx

Fan
Min
xxxxxxxx xx001xxx xxxxxxxx xxxxxxxx xxxxxxxx
Med
xxxxxxxx xx010xxx xxxxxxxx xxxxxxxx xxxxxxxx
Max
xxxxxxxx xx011xxx xxxxxxxx xxxxxxxx xxxxxxxx
Auto
xxxxxxxx xx100xxx xxxxxxxx xxxxxxxx xxxxxxxx
NONE/Auto mode
xxxxxxxx xx000xxx xxxxxxxx xxxxxxxx xxxxxxxx

Mode
Auto
xxxxxxxx xxxxx010 xxxxxxxx xxxxxxxx xxxxxxxx
Cool
xxxxxxxx xxxxx000 xxxxxxxx xxxxxxxx xxxxxxxx
Dry
xxxxxxxx xxxxx001 xxxxxxxx xxxxxxxx xxxxxxxx
Heat
xxxxxxxx xxxxx011 xxxxxxxx xxxxxxxx xxxxxxxx
Fan
xxxxxxxx xxxxx100 xxxxxxxx xxxxxxxx xxxxxxxx

Power
On
xxxxxxxx 1xxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx
Off
xxxxxxxx 0xxxxxxx xxxxxxxx xxxxxxxx xxxxxxxx

LED
10100001 10011000 01000101 11111111 11111111
```

## Decoding

## Encoding
