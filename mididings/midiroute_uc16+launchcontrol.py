from mididings import *
from mididings.extra.gm import *
from synth import *

# MIDI constants defined in mididings.extra.gm
#
#   CTRL_NRPN_MSB       99 (0x63)
#   CTRL_NRPN_LSB       98 (0x62)
#   CTRL_DATA_ENTRY_MSB  6 (0x06)
#   CTRL_DATA_ENTRY_LSB 38 (0x26)

# mininova = Synth()

config(
    backend="alsa",
    in_ports = [
        ('incoming uc16','UC-16 USB MIDI Controller:0'),
        # ('nanopad in', 'nanoPAD:0')
        ('incoming launchcontrol','Launch Control:0')
    ],
    out_ports = [
        ('midisport b out','MidiSport 2x2:1')
    ]
)

run(
    # split functionality by physical control surface
    PortSplit({

        # Control Surface : Evolution U-Control UC-16 preset 1

        'incoming uc16' : [

            # Evolution U-Control UC-16 preset 1

            # UC16 Knob  1 (CC  1) ->   (CC  75) Novation Mininova : Filter 1 Frequency
            CtrlFilter(1) >> CtrlMap(1,74),
            # UC16 Knob  2 (CC  2) ->   (CC  71) Novation Mininova : Filter 1 Resonance
            CtrlFilter(2) >> CtrlMap(2,71),
            # UC16 Knob  3 (CC  3) ->   (CC  68) Novation Mininova : Filter 1 Type (14 Types)
            CtrlFilter(3) >> CtrlMap(3,68) >> CtrlRange(68,0,13,0,127),
            # UC16 Knob  4 (CC  4) ->   (CC  63) Novation Mininova : Filter 1 Drive
            CtrlFilter(4) >> CtrlMap(4,63),
            # UC16 Knob  5 (CC  5) -> (NRPN 0 1) Novation Mininova : Envelope 2 (Filter) Attack
            CtrlFilter(5) >> [ Ctrl(CTRL_NRPN_MSB,0), Ctrl(CTRL_NRPN_LSB,1), CtrlMap(5,CTRL_DATA_ENTRY_MSB) ],
            # UC16 Knob  6 (CC  6) -> (NRPN 0 2) Novation Mininova : Envelope 2 (Filter) Decay
            CtrlFilter(6) >> [ Ctrl(CTRL_NRPN_MSB,0), Ctrl(CTRL_NRPN_LSB,2), CtrlMap(6,CTRL_DATA_ENTRY_MSB) ],
            # UC16 Knob  7 (CC  7) -> (NRPN 0 3) Novation Mininova : Envelope 2 (Filter) Sustain
            CtrlFilter(7) >> [ Ctrl(CTRL_NRPN_MSB,0), Ctrl(CTRL_NRPN_LSB,1), CtrlMap(7,CTRL_DATA_ENTRY_MSB) ],
            # UC16 Knob  8 (CC  8) -> (NPRN 0 4) Novation Mininova : Envelope 2 (Filter) Release
            CtrlFilter(8) >> [ Ctrl(CTRL_NRPN_MSB,0), Ctrl(CTRL_NRPN_LSB,1), CtrlMap(8,CTRL_DATA_ENTRY_MSB) ],
            # UC16 Knob  9 (CC  9) ->   (CC  73) Novation Mininova : Envelope 1 (Amp) Attack
            CtrlFilter(9) >> CtrlMap(9,73),
            # UC16 Knob 10 (CC 10) ->   (CC  70) Novation Mininova : Envelope 1 (Amp) Decay
            CtrlFilter(10) >> CtrlMap(10,70),
            # UC16 Knob 11 (CC 11) ->   (CC  63) Novation Mininova : Envelope 1 (Amp) Sustain
            CtrlFilter(11) >> CtrlMap(11,63),
            # UC16 Knob 12 (CC 12) ->   (CC  72) Novation Mininova : Envelope 1 (Amp) Release
            CtrlFilter(12) >> CtrlMap(12,72),
            # UC16 Knob 13 (CC 13) -> 
            # UC16 Knob 14 (CC 14) ->
            # UC16 Knob 15 (CC 15) ->
            # UC16 Knob 16 (CC 16) -> Novation Mininova CC 79 : Envelope 2 (Filter) to Frequency Amount
            CtrlFilter(16) >> CtrlMap(16,79)
        ] >> Output('midisport b out',1),

        # Control Surface : Novation LaunchControl 

        'incoming launchcontrol' : [
            Split({
                CTRL : [
                    # Launchcontrol Knob  1   (CC 21)
                    # Launchcontrol Knob  2   (CC 22)
                    # Launchcontrol Knob  3   (CC 23)
                    # Launchcontrol Knob  4   (CC 24)
                    # Launchcontrol Knob  5   (CC 25)
                    # Launchcontrol Knob  6   (CC 26)
                    # Launchcontrol Knob  7   (CC 27)
                    # Launchcontrol Knob  8   (CC 28)
                    # Launchcontrol Knob  9   (CC 41)
                    # Launchcontrol Knob 10   (CC 42)
                    # Launchcontrol Knob 11   (CC 43)
                    # Launchcontrol Knob 12   (CC 44)
                    # Launchcontrol Knob 13   (CC 45)
                    # Launchcontrol Knob 14   (CC 46)
                    # Launchcontrol Knob 15   (CC 47)
                    # Launchcontrol Knob 16   (CC 48)

                    # LaunchControl Key up    (CC114)
                    CtrlFilter(114) >> CtrlValueFilter(127) >> NoteOn(60,127),
                    # LaunchControl Key down  (CC115)
                    CtrlFilter(115) >> CtrlValueFilter(127) >> NoteOff(60,0),
                    # LaunchControl Key left  (CC116)
                    CtrlFilter(116) >> CtrlValueFilter(127) >> [ Ctrl(CTRL_NRPN_MSB,63), Ctrl(CTRL_NRPN_LSB,0), Ctrl(CTRL_DATA_ENTRY_MSB,0) ],
                    # LaunchControl Key right (CC117)
                    CtrlFilter(117) >> CtrlValueFilter(127) >> [ Ctrl(CTRL_NRPN_MSB,63), Ctrl(CTRL_NRPN_LSB,0), Ctrl(CTRL_DATA_ENTRY_MSB,2) ]
                ],    
                NOTE: [
                    # LaunchControl Pad 1 (Note  9) -> (NRPN 0 122) Novation Mininova : Arppegiator ON/OFF (46=Off,47=0n)
                    Filter(NOTEON) >> KeyFilter(9) >> [ Ctrl(CTRL_NRPN_MSB,0), Ctrl(CTRL_NRPN_LSB,122), Process(toggle) ],                    
                    # LaunchControl Pad 2 (Note 10)
                    # LaunchControl Pad 3 (Note 11)
                    # LaunchControl Pad 4 (Note 12)
                    # LaunchControl Pad 5 (Note 25)
                    # LaunchControl Pad 6 (Note 26)
                    # LaunchControl Pad 7 (Note 27)
                    # LaunchControl Pad 8 (Note 28)
                ]
            }) >> Print('out') >> Output('midisport b out',1)
        ]

    })
)
