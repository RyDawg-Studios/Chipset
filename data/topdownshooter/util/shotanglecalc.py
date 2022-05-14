import numpy as np
import matplotlib.pyplot as plt
# %matplotlib widget
plt.style.use("dark_background")

N = 200

uniform_max_degs = 20
# that's the std to use for the normal one that makes these two have equal variant, for a fair comparison
equivalent_std = uniform_max_degs/np.sqrt(3)

rng = np.random.default_rng()
angles1 = rng.uniform(low=-uniform_max_degs, high=uniform_max_degs, size=N)
angles2 = rng.normal(scale=equivalent_std, size=N)
angles3 = np.clip(rng.normal(scale=equivalent_std, size=N), -equivalent_std*3, equivalent_std*3)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ang, ax in zip([angles1, angles2, angles3], axes):
    degs_to_rads = np.pi/180
    radii = rng.uniform(0, 1, N)
    X = np.sin(ang*degs_to_rads)*radii
    Y = np.cos(ang*degs_to_rads)*radii
    ax.scatter(X, Y, s=1.5)
    ax.set_ylim(0, 1.1)
    ax.set_xlim(-1.1, 1.1)

plt.show()