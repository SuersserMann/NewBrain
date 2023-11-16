import matplotlib.pyplot as plt

##ex1
import numpy as np

x = np.arange(0, 3, 0.01)
y = np.sin(2 * np.pi * x)
z = np.cos(2 * np.pi * x)

plt.rcParams.update({'font.size': 22})
fig = plt.figure(figsize=(12, 8))
plt.plot(x, y, lw=3, label=r"$\sin(2\pi x)$")
plt.plot(x, z, lw=3, label=r"$\cos(2\pi x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([0, 3])
plt.ylim([-1.1, 1.1])
plt.legend(loc="upper center")
plt.savefig("ex1.png", dpi=fig.dpi)
plt.close()

##ex2
x = np.arange(0, 3, 0.01)
y = np.sin(2.5 * np.pi * x)
z = np.sin(2 * np.pi * x)

plt.rcParams.update({'font.size': 14})

plt.plot(x, y, lw=3, c="C1")
plt.plot(x, z, lw=3, c="C1")
plt.fill_between(x, y, z)

plt.xlabel("x")
plt.ylabel("y")
plt.xlim([0, 3])
plt.ylim([-1.1, 1.1])
plt.tight_layout()
plt.savefig("ex2.png", dpi=fig.dpi)
plt.close()

# ex3
x = [1, 2, 3, 4, 5, 6]
y1 = [1, 3, 4, 5, 6, 3]
y2 = [3, 4, 2, 1, 4, 1]
y3 = [1, 2, 1, 1, 0, 1]
y4 = [0, 0, 0, 3, 4, 5]

plt.stackplot(x, y1, y2, y3, y4)
plt.savefig("ex3.png", dpi=fig.dpi)
plt.close()

# ex4
x = np.linspace(0, np.pi * 2, 31)
y = np.exp(np.sin(x))

plt.stem(x, y, bottom=1)
plt.savefig("ex4.png", dpi=fig.dpi)
plt.close();

# ex5
x = [1.3, 2.25, 2.9, 3.9, 5.1]
x_error = [0.4, 0.3, 0.2, 0.2, 0.1]
y = [1.1, 1.9, 3.1, 4, 5]
y_error = [0.45, 0.33, 0.3, 0.22, 0.14]
plt.scatter(x, y)
plt.errorbar(x, y, yerr=y_error, xerr=x_error, ls='none', capsize=3)
plt.savefig("ex5.png", dpi=fig.dpi)
plt.close()

# ex6
values = {
    "Group 1": [20, 10, 13, 17, 50],
    "Group 2": [10, 15, 17, 32, 26]
}

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 120)
plt.box(on=None)

for r, (n, v) in enumerate(values.items()):
    data = np.array(v)
    data_cum = data.cumsum(axis=0)
    colors = plt.cm.RdYlGn(np.linspace(0.15, 0.85, len(data)))

    for i, color in enumerate(colors):
        start = data_cum[i] - data[i]
        ax.barh(n, data[i], left=start, height=0.5, color=color, label=n)
        center = start + data[i] / 2
        ax.text(center, r, str(data[i]), ha='center', va='center')

plt.savefig("ex6.png", dpi=fig.dpi)
plt.close()

# ex7.
from matplotlib.gridspec import GridSpec

fig = plt.figure(constrained_layout=True, figsize=(12, 12))
gs = GridSpec(4, 4, figure=fig, left=0, bottom=0, right=1, top=1, wspace=0, hspace=0.)

for i in range(4):
    for j in range(4):
        b = '{:04b}'.format(i * 4 + j)
        B = [[int(b[0]), int(b[1])], [int(b[2]), int(b[3])]]

        ax = fig.add_subplot(gs[i, j])
        ax.imshow(B, cmap='binary', vmin=0, vmax=1.5)

        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        ax.hlines(0.5, -0.5, 1.5, color='k')
        ax.vlines(0.5, -0.5, 1.5, color='k')

plt.savefig("ex7.png", dpi=fig.dpi)

