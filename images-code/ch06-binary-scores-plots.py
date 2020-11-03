#!/usr/bin/env python3

# This python script is used to generate the image used in Chapter 6 to
# plot and visualize the semantic similarity scores of binarized word vectors
# (for dict2vec, fasttext and GloVe) as well as the scores of original
# real-valued vectors. The corresponding image is ch06-binary-scores-plots.pdf.

import matplotlib.pyplot as plt

bits_size = [64, 128, 256, 512]

# `X_average` is Fisher average of 64, 128, 256 and 512 bits
d2v_baseline = 0.588
d2v_average  = [0.465, 0.541, 0.553, 0.54]

ft_baseline = 0.595
ft_average  = [0.389, 0.524, 0.575, 0.577]

gl_baseline = 0.494
gl_average  = [0.263, 0.397, 0.470, 0.487]

# 3 plots stacked up vertically (so 1 column and 3 rows).
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

# Plot of binarized Dict2vec vectors (in ax1, which is top plot).
ax1.plot(bits_size, d2v_average, 'b', lw=0.8, label="binarized", marker="x")
ax1.axhline(d2v_baseline, color="k", ls='--', lw=0.8, label="raw (9600 bits)")
ax1.set_xticks(bits_size)
ax1.set_ylim(0.20, 0.65)
ax1.set_yticks([0.25, 0.35, 0.45, 0.55])
ax1.legend(loc=4)
ax1.set_title("dict2vec")
ax1.set_xlabel("Binary vector size [in number of bits]")
ax1.set_ylabel("Average semantic\nsimilarity score")

# Plot of binarized Fasttext vectors (in ax2, which is middle plot).
ax2.plot(bits_size, ft_average, 'b', lw=0.8, label="binarized", marker="x")
ax2.axhline(ft_baseline, color="k", ls='--', lw=0.8, label="raw (9600 bits)")
ax2.set_xticks(bits_size)
ax2.set_ylim(0.20, 0.65)
ax2.set_yticks([0.25, 0.35, 0.45, 0.55])
ax2.legend(loc=4)
ax2.set_title("fasttext")
ax2.set_xlabel("Binary vector size [in number of bits]")
ax2.set_ylabel("Average semantic\nsimilarity score")

# Plot of binarized GloVe vectors (in ax3, which is bottom plot).
ax3.plot(bits_size, gl_average, 'b', lw=0.8, label="binarized", marker="x")
ax3.axhline(gl_baseline, color="k", ls='--', lw=0.8, label="raw (9600 bits)")
ax3.set_xticks(bits_size)
ax3.set_ylim(0.20, 0.65)
ax3.set_yticks([0.25, 0.35, 0.45, 0.55])
ax3.legend(loc=4)
ax3.set_title("GloVe")
ax3.set_xlabel("Binary vector size [in number of bits]")
ax3.set_ylabel("Average semantic\nsimilarity score")

plt.show()
