#!/usr/bin/env python3
import numpy as np
a = np.array([0], dtype=int)
val = int(input("Oh Oh Oh I got a 0hverflow in my integer!\n"))
if val == -1:
	exit()
a[0] = val
a[0] = (a[0] * 7) + 1
print(a[0])
if a[0] == -1:
	print("VHC2022{" + str(val) + "}\n")