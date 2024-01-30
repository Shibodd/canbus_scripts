import matplotlib.pyplot as plt
import numpy as np

BITS = "010001011010100010001" # Encoded message
FCAN = 8 # MHz
TQ_PER_BIT = 1 + 13 + 2 # sync_seg + prop_seg + phase_seg1 + phase_seg2

tq_duration = 1/FCAN # us (fcan is in MHz)
bit_duration = TQ_PER_BIT * tq_duration # us

ys = np.array([int(y) for y in BITS])
xs = np.arange(len(ys), dtype=int)
ts = bit_duration * xs

canh = 2.5 + (1 - ys)
canl = 2.5 - (1 - ys)

plt.subplot(2, 1, 1)
plt.step(ts, canh, where='post', label='CANH')
plt.step(ts, canl, where='post', label='CANL')
plt.xlabel("Time [us]")
plt.ylabel("Voltage [V]")
plt.legend()
plt.xticks(ts)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.step(xs, ys, where='post', label='Message')
plt.xlabel("Index in message")
plt.ylabel("Bit value")
plt.xticks(xs)
plt.yticks([0, 1])
plt.grid(True)

plt.show()

