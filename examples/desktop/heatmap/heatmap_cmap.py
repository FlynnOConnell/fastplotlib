"""
Heatmap change cmap
===================
Change the cmap of a heatmap
"""


# test_example = false
# sphinx_gallery_pygfx_docs = 'hidden'

import fastplotlib as fpl
import numpy as np

figure = fpl.Figure()

xs = np.linspace(0, 1_000, 10_000, dtype=np.float32)

sine = np.sin(np.sqrt(xs))

data = np.vstack([sine * i for i in range(20_000)])

# plot the image data
img = figure[0, 0].add_image(data=data, name="heatmap")

figure.show()

figure.canvas.set_logical_size(700, 560)

figure[0, 0].auto_scale()

img.cmap = "viridis"

# NOTE: `if __name__ == "__main__"` is NOT how to use fastplotlib interactively
# please see our docs for using fastplotlib interactively in ipython and jupyter
if __name__ == "__main__":
    print(__doc__)
    fpl.run()
