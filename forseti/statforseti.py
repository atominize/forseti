# Statistic for forseti
# Use python3 to run

import statistics
import matplotlib.pyplot as plt

x = [1, 2, 5, 6]
y = statistics.mean(x)
z = statistics.stdev(x)

print(z)
plt.plot(x)
plt.show()
