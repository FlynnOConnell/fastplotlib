"""
Heatmap change data
===================
Change the data of a heatmap
"""

# test_example = false
# sphinx_gallery_pygfx_docs = 'hidden'

import fastplotlib as fpl
import numpy as np

figure = fpl.Figure(size=(700, 560))

xs = np.linspace(0, 1_000, 9_000, dtype=np.float32)

sine = np.sin(np.sqrt(xs))

data = np.vstack([sine * i for i in range(9_000)])

# plot the image data
img = figure[0, 0].add_image(data=data, name="heatmap")

figure.show()

cosine = np.cos(np.sqrt(xs)[:3000])

# change first 2,000 rows and 3,000 columns
img.data[:2_000, :3_000] = np.vstack([cosine * i * 4 for i in range(2_000)])

# NOTE: `if __name__ == "__main__"` is NOT how to use fastplotlib interactively
# please see our docs for using fastplotlib interactively in ipython and jupyter
if __name__ == "__main__":
    print(__doc__)
    fpl.run()
