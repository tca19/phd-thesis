#!/usr/bin/env python3

# This python script is used to generate the image used in Chapter 1 to
# visualize analogies in a word embedding vector space of two dimensions.
# The corresponding image is ch01-word-analogy.pdf.

import numpy as np
import matplotlib.pyplot as plt

# A word embedding is represented as a single point in this example. Then, an
# analogy is represented as a vector between two points which share a common
# link. Three different couples of related embeddings are displayed:
#   - Germany and Berlin
#   - Hungary and Budapest
#   - Norway  and Oslo
# The common link (= the common analogy, represented as a vector) is the
# relation "is the capital of".
# Values of vectors are not based on any pre-trained embeddings (I created them
# for this example).
germany  = (-0.25,  0.75)
berlin   = ( 0.70,  0.30)
hungary  = (-0.55,  0.55)
budapest = ( 0.33, -0.10)
norway   = (-0.40, -0.15)
oslo     = ( 0.55, -0.40)

# Plot the embeddings. Countries are plotted in blue and cities are plotted in
# magenta. The marker 'o' is to plot them as filled circle.
plt.plot(germany[0] , germany[1] , color="blue", marker='o')
plt.plot(hungary[0] , hungary[1] , color="blue", marker='o')
plt.plot(norway[0]  , norway[1]  , color="blue", marker='o')
plt.plot(berlin[0]  , berlin[1]  , color="magenta", marker='o')
plt.plot(budapest[0], budapest[1], color="magenta", marker='o')
plt.plot(oslo[0]    , oslo[1]    , color="magenta", marker='o')

# Display the name of each country/city on top of its respective point. The
# offset depends for each point and is made so the text appears centered on top
# of the point.
plt.text(germany[0]  - 0.13, germany[1]  + 0.06, "Germany",  fontsize=12)
plt.text(berlin[0]   - 0.08, berlin[1]   + 0.07, "Berlin" ,  fontsize=12)
plt.text(hungary[0]  - 0.11, hungary[1]  + 0.06, "Hungary",  fontsize=12)
plt.text(budapest[0] - 0.08, budapest[1] + 0.07, "Budapest", fontsize=12)
plt.text(norway[0]   - 0.10, norway[1]   + 0.06, "Norway",   fontsize=12)
plt.text(oslo[0]     - 0.06, oslo[1]     + 0.06, "Oslo",     fontsize=12)

# Draw arrows between related embeddins (country and its respective capital).
plt.annotate("", xy=(germany[0] + 0.02, germany[1] - 0.01),
                 xytext=(berlin[0] - 0.02, berlin[1] + 0.01),
                 arrowprops=dict(arrowstyle="->"))
plt.annotate("", xy=(hungary[0] + 0.02, hungary[1] - 0.01),
                 xytext=(budapest[0] - 0.02, budapest[1] + 0.01),
                 arrowprops=dict(arrowstyle="->"))
plt.annotate("", xy=(norway[0] + 0.02, norway[1] - 0.01),
                 xytext=(oslo[0] - 0.02, oslo[1] + 0.01),
                 arrowprops=dict(arrowstyle="->"))

# Needs to be set manually because if we let matplotlib choose the approriate
# limits, some texts are outside the drawing area.
plt.axis([-0.75, 0.8, -0.5, 1])
plt.show()
