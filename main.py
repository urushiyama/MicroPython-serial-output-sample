import math

from machine import Timer

tim = Timer()
sec = 0.0
amp = 0.49
freq = 1


def generate_sine(sec, amp, freq):
    return amp * (math.sin(2.0 * math.pi * freq * sec / 1000) + 1.0)


def tick(timer):
    global sec, amp, freq
    print(", ".join([str(generate_sine(sec, amp, freq * (i + 1))) for i in range(16)]))
    sec += 1

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
