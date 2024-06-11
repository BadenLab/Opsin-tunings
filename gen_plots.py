import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

sns.set_context('talk')
sns.set_theme(style="white")

opsins = np.load(r"AllOpsins.npy")
zeb_ops = [355, 416, 467, 558]
led_wvs = [365, 420, 470, 588]
colours = np.flip(["#ef8e00", "teal","#5600fe", "fuchsia"])
ops_name = ["SWS1", "SWS2", "RH2", "LWS1"]

#Plot heatmap
fig, ax = plt.subplots(1, 1, figsize = (8, 4), dpi = 200)
plt.imshow(opsins, cmap = "Greys_r")
for n, i in enumerate(zeb_ops):
    plt.axhline(i, c = colours[n], label = f"{ops_name[n]}")
plt.ylabel("Opsin template (nm)")
plt.xlabel("Wavelength (nm)")
cbar = plt.colorbar()
cbar.set_label('Rel. absorption', rotation=90)
cbar.ax.get_yaxis().labelpad = 5
cbar.ax.set_yticks([0, .25, .5, .75, 1], [0, .25, .5, .75, 1])
plt.tight_layout()
plt.legend()

# Plot opsin profile
fig, ax = plt.subplots(1, 1, figsize = (8, 4), dpi = 200)
for n, i in enumerate(zeb_ops):
    line = opsins[i]
    ysmoothed = scipy.ndimage.filters.gaussian_filter1d(line, sigma=2)   
    plt.plot(ysmoothed, c =colours[n], label = f"{ops_name[n]}")
plt.xlim(250, 700)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Rel. absorption")
for n, i in enumerate(zeb_ops):
    plt.axvspan(led_wvs[n], led_wvs[n]+10, color = colours[n], alpha = .33, lw = 0, label = f"LED {led_wvs[n]}")

legs_labels = plt.gca().get_legend_handles_labels()
opsin_labels = legs_labels[1][:4]
opsin_handles = legs_labels[0][:4]
leds_labels = legs_labels[1][4:]
leds_handles = legs_labels[0][4:]

leg1 = plt.legend(opsin_handles, opsin_labels, title = "Opsins", bbox_to_anchor=(1.2, .9), loc=0)
leg2 = plt.legend(leds_handles, leds_labels, title = "LEDs", bbox_to_anchor=(1.23, .5), loc=0)
ax.add_artist(leg1)
plt.tight_layout()

plt.show()
