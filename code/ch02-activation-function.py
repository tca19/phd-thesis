#!/usr/bin/env python3

# This python script is used to generate the image used in Chapter 2 to
# represent and show the different activation functions one can used in a
# neural network. The corresponding image is ch02-activation-function.pdf.

import numpy as np
import matplotlib.pyplot as plt

# No need to go further than [-3, 3], it is enough to visualize the differences
# between the functions.
x = np.linspace(-3, 3, 10001)

# 4 functions plotted:
#   - Identity
#   - Sigmoid
#   - Hyperbolic tangent
#   - ReLu
plt.plot(x, x, label="Identity")
plt.plot(x, 1 / (1 + np.exp(-x)), label="Sigmoid")
plt.plot(x, np.tanh(x), label="Hyperbolic tangent")
plt.plot(x, np.maximum(0, x), label="ReLU")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
