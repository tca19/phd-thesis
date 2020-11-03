#!/usr/bin/env python3

# This python script is used to generate the image used in Chapter 1 to
# visualize some embeddings in a 2D plan. Word embeddings of related terms are
# grouped in the same area of the plan. The corresponding image is
# ch01-embeddings2D-plan.pdf.

import numpy as np
import matplotlib.pyplot as plt

# Six different word embeddings. 1 word embedding = 1 point in a 2D space so
# each one of them has two coordinates. Two groups: cooking ingredients and
# football.
milk      = ("milk",      np.array([0.8 ,  1.3]))
flour     = ("flour",     np.array([1   ,  1.9]))
lumps     = ("lumps",     np.array([0.7 ,  1.7]))
liverpool = ("Liverpool", np.array([-0.6,  0.1]))
tottenham = ("Tottenham", np.array([-0.4,  0.6]))
goal      = ("goal",      np.array([-0.2, -0.1]))

# Plot the embeddings as red filled circles and display their name on top of it.
for (text, (x, y)) in [milk, flour, lumps, liverpool, tottenham, goal]:
    plt.plot(x, y, color="red", marker='o')
    plt.text(x - 0.1, y + 0.1, text, fontsize=12)

# Needs to be set manually because if we let matplotlib choose the approriate
# limits, some texts are outside the drawing area.
plt.axis([-1, 1.5, -1, 2.5])
plt.show()
