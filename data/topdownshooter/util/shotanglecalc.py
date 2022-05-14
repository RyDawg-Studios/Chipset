import numpy as np
import matplotlib.pyplot as plt
# %matplotlib widget
plt.style.use("dark_background")

N = 100000
n = 100  # histogram bin count along each dimension

uniform_max_degs = 30
clamp_sigma = 3
# that's the std to use for the normal one that makes these two have equal variant, for a fair comparison
equivalent_std = uniform_max_degs/np.sqrt(3)


def normal_clamped_resample(mu=0, sigma=1, size=1, clamp_sigmas=2):
    """
        Normal distribution that guarantees no outliers futher than clamp_sigmas STDs.
        This is done by rerolling such outliers once, and clamping them if that doesn't help.
    """
    arr = rng.normal(loc=mu, scale=sigma, size=size)
    # find bad positions:
    inds = (arr < mu-clamp_sigmas*sigma) | (arr > mu+clamp_sigmas*sigma)
    to_resample = inds.sum()
    arr[inds] = rng.normal(loc=mu, scale=sigma, size=to_resample)
    # and finally clamp just in case, but should rarely ever be required
    return np.clip(arr, mu-clamp_sigmas*sigma, mu+clamp_sigmas*sigma)


rng = np.random.default_rng()
angles1 = rng.uniform(low=-uniform_max_degs, high=uniform_max_degs, size=N)
angles2 = rng.normal(scale=equivalent_std, size=N)
angles3 = normal_clamped_resample(sigma=equivalent_std, size=N, clamp_sigmas=clamp_sigma)

fig, axes = plt.subplots(3, 1, figsize=(10, 20))
for ang, ax in zip([angles1, angles2, angles3], axes):
    ax: plt.Axes
    degs_to_rads = np.pi/180
    radii = np.sqrt(rng.uniform(0, 4, N))
    X = np.sin(ang*degs_to_rads)*radii
    Y = np.cos(ang*degs_to_rads)*radii
    H, xedges, yedges = np.histogram2d(X, Y, bins=n)
    ax.imshow(np.flipud(H.T), extent=(xedges[0], xedges[-1], yedges[0], yedges[-1]), interpolation="bicubic")
    ax.set_ylim(0, 1.1)
    ax.set_xlim(-1.1, 1.1)
    ax.set_aspect(1)
axes[0].set_title(f"Uniform, $\pm${uniform_max_degs} degrees")
axes[1].set_title(f"Normal, std of {equivalent_std:.1f} degrees")
axes[2].set_title(f"Normal, std of {equivalent_std:.1f} degrees, resamples/clamped to $\pm {clamp_sigma} \sigma$")
# plt.legend()
plt.show()
plt.savefig("spread_patterns_heatmap.png")