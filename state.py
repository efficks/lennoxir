from bitarray import bitarray
from enum import Enum

class Mode(Enum):
    COOL = bitarray('000')
    DRY  = bitarray('001')
    AUTO = bitarray('010')
    HEAT = bitarray('011')
    FAN  = bitarray('100')

class FanSpeed(Enum):
    NONE = bitarray('000')
    MIN  = bitarray('001')
    MED  = bitarray('010')
    MAX  = bitarray('011')
    AUTO = bitarray('100')

class State(object):
    def __init__(self):
        pass

class StateOff(State):
    def __init__(self):
        pass

    def __str__(self):
        return "OFF"

    def data(self):
        return "1010000100000000010000001111111111111111"

class StateOn(State):
    def __init__(self, mode, temperature, fanSpeed):
        self.__mode = mode
        self.__temperature = temperature
        self.__fanSpeed = fanSpeed

    def __str__(self):
        return "ON Mode:{} Temperature:{} Fan:{}".format(self.__mode.name, self.__temperature, self.__fanSpeed.name)

    def data(self):

        t = bitarray()
        t.frombytes(bytes([self.__temperature-17]))
        
        data = bitarray("1010000110{}{}0100{}1111111111111111".format(
            self.__fanSpeed.value.to01(),
            self.__mode.value.to01(),
            t.to01()[-4:],
        ))
        return data
