from synthesizer import synthesize
from notes import *

# Beats per minute
BPM = 100
# Duration (in seconds) for a quarter note
qNote = 60/BPM
# Duration (in seconds) for a half, 1/8, 1/16 and 1/32 notes
hNote, eNote, sNote, tNote = (qNote*2, qNote/2, qNote/4, qNote/8)

initOnset = 0.5

# Track ID, Onset time, MIDI note nunmber, Velocity (0-127), Gate time (s)
midiData = [[1, initOnset,
             noteToNumber("D", 5), 50, hNote],
            [1, initOnset+hNote,
             noteToNumber("B", 4), 50, qNote],
            [1, initOnset+hNote+qNote,
             noteToNumber("B", 4), 50, qNote],
            [1, initOnset+hNote+qNote+qNote+qNote,
             noteToNumber("G", 4), 50, hNote],
            [1, initOnset+hNote+qNote+qNote+qNote+hNote+tNote,
             noteToNumber("B", 4), 50, qNote-tNote]]
midiData2 = [[1, initOnset,
             noteToNumber("F", 3), 35, hNote],
            [1, initOnset+hNote,
             noteToNumber("D", 3), 35, qNote],
            [1, initOnset+hNote+qNote,
             noteToNumber("D", 3), 35, qNote],
            [1, initOnset+hNote+qNote+qNote+qNote,
             noteToNumber("B", 2), 35, hNote],
            [1, initOnset+hNote+qNote+qNote+qNote+hNote+tNote,
             noteToNumber("D", 3), 35, qNote-tNote]]
synthesize(midiData, "piano", "cassiopeia-piano.wav")
synthesize(midiData2, "cello", "cassiopeia-cello.wav")

