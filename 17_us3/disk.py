import numpy as np

speed_3 = np.array([0, 33, 37, 42, 45, 48, 48, 42, 37, 34, 34, 39, 35, 40, 38])
speed_5 = np.array([70, 90, 100, 110, 115, 108, 100, 82, 80, 80, 90, 98, 98, 90])

print(f"speed 3:  {np.mean(speed_3):.0f} +- {np.std(speed_3):.0f}")
print(f"speed 5:  {np.mean(speed_5):.0f} +- {np.std(speed_5):.0f}")