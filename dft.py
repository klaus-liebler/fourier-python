import numpy as np
import matplotlib.pyplot as plt

time=np.linspace(0,2*np.pi,256)
amplitude = np.sin(3.5*time)

T = time[1] - time[0]  # sampling interval 
N = amplitude.size
windowing = np.ones(N)
#windowing = np.hanning(N)
amplitude = windowing*amplitude

fft = np.fft.fft(amplitude)
abs=np.abs(fft)[0:N//2] * 1 / N
# 1/T = Frequenz in Hertz
freq = np.linspace(0, 1/(2*T), N//2)



fig, (ax1, ax2) = plt.subplots(2, 1)
# make a little extra space between the subplots
fig.subplots_adjust(hspace=0.5)
fig.set_figwidth(10)


# Plot a sine wave using time and amplitude obtained for the sine wave
ax1.plot(time, windowing)
ax1.plot(time, amplitude)
ax1.axis([0, 2*np.pi, -1.1, +1.1])
# Give a title for the sine wave plot

# Give x axis label for the sine wave plot
ax1.set_xlabel('Zeit')
# Give y axis label for the sine wave plot
ax1.set_ylabel('Amplitude')
ax1.grid(True, which='both')
ax1.axhline(y=0.0, color="grey")

ax2.set_ylabel("Energie")
ax2.set_xlabel("Frequenz [Hz]")
ax2.bar(freq[0:N//2], np.abs(fft)[0:N//2]/N, 0.1)  # 1 / N is a normalization factor
plt.show()
