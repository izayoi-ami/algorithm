##
import numpy as np

INPUT="250 100 70 30 110 6 210 66 73 32 102 76 19 115 79 30 96 78 27 110 72 37 31 64 33 113 250 37 110 70 40 104 72 25 31 78 26 100 250 249 96 71 20 104 78 210 98 66 19 107 70 23 109 65 23 45 250 2 107 63 19 114 63 210 114 63 32 99 250 43 110 79 36 31 77 33 107 79 38 104 73 32 31 59 32 99 250 245 85 250 38 110 250 27 98 59 32 98 73 22 100 26 25 96 71 20 104 78 36 100 77 23 96 76 21 103 8 21 110 71 210 112 79 33 115 67 32 102 250 36 100 64 23 113 63 32 98 63 236 31 62 19 48 15 234 54 14 226 101 17 224"

NUMS = map(int, INPUT.strip().split(" "))

offsets = [78,1,38]
shifted = [(v+offsets[i%3])%256 for i,v in enumerate(NUMS)]
print("".join(map(chr,shifted)))


"da158740f7"

##
