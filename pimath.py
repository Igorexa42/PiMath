from mpmath import mp
import sys

mp.dps = sys.argv[1]
pi = str(+mp.pi)
print(pi)
