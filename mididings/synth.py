from mididings import *
from mididings.extra.gm import *

class NRPN :
    def __init__(self) :
        self.CTRL_MSB = 0
        self.CTRL_LSB = 0
        self.DATA_MSB = 0
        self.DATA_LSB = 0

class switch :
    def __init__(self) :
        self.on  = 0
        self.off = 0

class parameter :
    def __init__(self) :
        self.NRPN = NRPN()
        self.switch = switch()

class Arpeggiator:
    def __init__(self) :
        self.run = False
        self.msg = parameter()
        # self.latch = False

# class Synth :
#    arp = Arpeggiator()

arp = Arpeggiator()

arp.msg.switch.on  = 47
arp.msg.switch.off = 46

def toggle(event):

    match arp.run :
        case True :
            value = arp.msg.switch.on
        case False :
            value = arp.msg.switch.off
    arp.run = not arp.run

    event.type = CTRL
    event.ctrl = CTRL_DATA_ENTRY_MSB
    event.value = value
    return event
