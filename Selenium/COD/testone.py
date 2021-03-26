import matplotlib.pyplot as plt
import numpy as np

x = np.arange(20)
y = np.sin(x)

fig, ax = plt.subplots()
line1 = ax.scatter(x[:10],y[:10],20, c="red", picker=True, marker='*')
line2 = ax.scatter(x[10:20],y[10:20],20, c="green", picker=True, marker='^')

ia = lambda i: plt.annotate("Annotate {}".format(i), (x[i],y[i]), visible=False)
img_annotations = [ia(i) for i in range(len(x))] 

lce = [False]
def show_ROI(event):
    tlce=False
    for annot, line in zip([img_annotations[:10],img_annotations[10:20]], [line1, line2]):
        if line.contains(event)[0]:
            lce[0]=tlce=True
            ind = line.contains(event)[1]["ind"]
            print('onpick3 scatter:', ind)
            ab = annot[ind[0]]
            ab.set_visible(True)
    if not tlce:
        for ab in img_annotations:
            ab.set_visible(False)
        lce[0] = False
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('button_press_event', show_ROI)

plt.show()