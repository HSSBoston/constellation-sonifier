import sound, time

stream = sound.init()

sound.beep(stream, 3)
time.sleep(2)

for i in range(5):
    sound.beep(stream, 1)
    time.sleep(1)

sound.close(stream)
