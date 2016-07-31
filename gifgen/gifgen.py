"""from PIL import ImageGrab
import time


time.sleep(5)
ImageGrab.grab().save("screen_capture01.png", "PNG")
ImageGrab.grab().save("screen_capture02.png", "PNG")
ImageGrab.grab().save("screen_capture03.png", "PNG")
ImageGrab.grab().save("screen_capture04.png", "PNG")
ImageGrab.grab().save("screen_capture05.png", "PNG")
ImageGrab.grab().save("screen_capture06.png", "PNG")
ImageGrab.grab().save("screen_capture07.png", "PNG")
ImageGrab.grab().save("screen_capture08.png", "PNG")
ImageGrab.grab().save("screen_capture09.png", "PNG")
ImageGrab.grab().save("screen_capture10.png", "PNG")
ImageGrab.grab().save("screen_capture11.png", "PNG")
ImageGrab.grab().save("screen_capture12.png", "PNG")
ImageGrab.grab().save("screen_capture13.png", "PNG")
ImageGrab.grab().save("screen_capture14.png", "PNG")
ImageGrab.grab().save("screen_capture15.png", "PNG")
ImageGrab.grab().save("screen_capture16.png", "PNG")
ImageGrab.grab().save("screen_capture17.png", "PNG")
ImageGrab.grab().save("screen_capture18.png", "PNG")
ImageGrab.grab().save("screen_capture19.png", "PNG")
ImageGrab.grab().save("screen_capture20.png", "PNG")
ImageGrab.grab().save("screen_capture21.png", "PNG")
ImageGrab.grab().save("screen_capture22.png", "PNG")
ImageGrab.grab().save("screen_capture23.png", "PNG")
ImageGrab.grab().save("screen_capture24.png", "PNG")
print "complete" 
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
l, = plt.plot([], [], 'k-o')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()