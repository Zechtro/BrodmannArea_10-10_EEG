import random
truth_table = """
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	1	1	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
1	0	0	1	1	1	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
1	1	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
1	1	0	1	1	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	1	1	1
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	1	1	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	1	1	0	0	0	1	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	1	0	0	0	0	0
0	0	0	0	0	1	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	1	1	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	1	0	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	1	0	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	1	0	0	0	0	1	1	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	1	1	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	1	0	0	0	0	1	1	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	1	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	1	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	1	0	0	1	1	1	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	1	1	0	0	0	1	1	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
1	1	1	0	0	0	0	1	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	1
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	1	1
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	1	1	0	0	1
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	1	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	1	0	0	0	0	0
0	0	0	0	0	1	0	0	0	0	0	1	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	1	0	0	0	0	0	0	1	1	0	0	0	0	0	0	1	0	0	0	0	0
0	1	0	0	0	1	1	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	1	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	1	1	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	1	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	1	1	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
"""

numToBADict = {
    1 : "BA1L",
    2 : "BA2L",
    3 : "BA3L",
    4 : "BA4L",
    5 : "BA5L",
    6 : "BA6L",
    7 : "BA7L",
    8 : "BA8L",
    9 : "BA9L",
    10 : "BA10L,",
    11 : "BA11L",
    12 : "BA17L",
    13 : "BA18L",
    14 : "BA19L",
    15 : "BA20L",
    16 : "BA21L",
    17 : "BA22L",
    18 : "BA23L",
    19 : "BA24L",
    20 : "BA31L",
    21 : "BA32L",
    22 : "BA37L",
    23 : "BA38L",
    24 : "BA39L",
    25 : "BA40L",
    26 : "BA41L",
    27 : "BA42L",
    28 : "BA44L",
    29 : "BA45L",
    30 : "BA46L",
    31 : "BA47L",
    32 : "BA1R",
    33 : "BA2R",
    34 : "BA3R",
    35 : "BA4R",
    36 : "BA5R",
    37 : "BA6R",
    38 : "BA7R",
    39 : "BA8R",
    40 : "BA9R",
    41 : "BA10R",
    42 : "BA11R",
    43 : "BA17R",
    44 : "BA18R",
    45 : "BA19R",
    46 : "BA20R",
    47 : "BA21R",
    48 : "BA22R",
    49 : "BA23R",
    50 : "BA24R",
    51 : "BA31R",
    52 : "BA32R",
    53 : "BA37R",
    54 : "BA38R",
    55 : "BA39R",
    56 : "BA40R",
    57 : "BA41R",
    58 : "BA42R",
    59 : "BA44R",
    60 : "BA45R",
    61 : "BA46R",
    62 : "BA47R",
}

# Mengubah truth_table dari kumpulan string menjadi dalam bentuk array
truth_table = truth_table.split("\n")
for i in range(0,len(truth_table)):
    truth_table[i] = truth_table[i].split("\t")

# Inisialisasi kondisi elektroda 10-10 EEG yang aktif
arr_activeElektrode = [0 for i in range(1,66)]

# Inisialisasi simulasi jumlah Brodmann Area yang aktif
n_active_BA = random.randint(1,5)

print("Banyak Area Brodmann yang aktif:",n_active_BA)

# Inisialisasi simulasi Brodmann Area yang aktif
print("Area Brodmann yang aktif:")
for i in range(0,n_active_BA):
    BA = random.randint(1,62)
    print(numToBADict[BA])
    for j in range(0,len(arr_activeElektrode)):
        arr_activeElektrode[j] = (int(arr_activeElektrode[j]) or int(truth_table[BA][j]))

print()        
print("List kondisi elektroda EEG (1 menandakan menerima impuls):")
print(arr_activeElektrode)
print()

# Hasil Area Brodmann yang aktif yang dideteksi dari kondisi elektroda 10-10 EEG
print("Area Brodmann yang terdeteksi:")
if (( int(arr_activeElektrode[20]) and int(arr_activeElektrode[31]) and int(arr_activeElektrode[32]) and int(arr_activeElektrode[42]) and int(arr_activeElektrode[43]))==1):
    print(numToBADict[1])
if ( int(arr_activeElektrode[20]) and int(arr_activeElektrode[31]) and int(arr_activeElektrode[32]) and int(arr_activeElektrode[42]) and int(arr_activeElektrode[43]))==1:
    print(numToBADict[2])
if ( int(arr_activeElektrode[19]) and int(arr_activeElektrode[20]) and int(arr_activeElektrode[30]) and int(arr_activeElektrode[31]) and int(arr_activeElektrode[42]))==1:
    print(numToBADict[3])
if ( int(arr_activeElektrode[20]) and int(arr_activeElektrode[21]) and int(arr_activeElektrode[31]) and int(arr_activeElektrode[32]) and int(arr_activeElektrode[42]))==1:
    print(numToBADict[4])
if ( int(arr_activeElektrode[31]) and int(arr_activeElektrode[32]) and int(arr_activeElektrode[33]) and int(arr_activeElektrode[43]) and int(arr_activeElektrode[44]))==1:
    print(numToBADict[5])
if ( int(arr_activeElektrode[10]) and int(arr_activeElektrode[11]) and int(arr_activeElektrode[20]) and int(arr_activeElektrode[21]) and int(arr_activeElektrode[31]))==1:
    print(numToBADict[6])
if ( int(arr_activeElektrode[42]) and int(arr_activeElektrode[43]) and int(arr_activeElektrode[49]) and int(arr_activeElektrode[50]) and int(arr_activeElektrode[51]))==1:
    print(numToBADict[7])
if ( int(arr_activeElektrode[4]) and int(arr_activeElektrode[5]) and int(arr_activeElektrode[10]) and int(arr_activeElektrode[11]) and int(arr_activeElektrode[12]))==1:
    print(numToBADict[8])
if ( int(arr_activeElektrode[0]) and int(arr_activeElektrode[3]) and int(arr_activeElektrode[4]) and int(arr_activeElektrode[5]) and int(arr_activeElektrode[10]))==1:
    print(numToBADict[9])
if ( int(arr_activeElektrode[0]) and int(arr_activeElektrode[1]) and int(arr_activeElektrode[3]) and int(arr_activeElektrode[4]) and int(arr_activeElektrode[5]))==1:
    print(numToBADict[10])
if ( int(arr_activeElektrode[0]) and int(arr_activeElektrode[1]) and int(arr_activeElektrode[3]) and int(arr_activeElektrode[4]) and int(arr_activeElektrode[8]))==1:
    print(numToBADict[11])
if ( int(arr_activeElektrode[58]) and int(arr_activeElektrode[59]) and int(arr_activeElektrode[62]) and int(arr_activeElektrode[63]) and int(arr_activeElektrode[64]))==1:
    print(numToBADict[12])
if ( int(arr_activeElektrode[57]) and int(arr_activeElektrode[58]) and int(arr_activeElektrode[59]) and int(arr_activeElektrode[62]) and int(arr_activeElektrode[63]))==1:
    print(numToBADict[13])
if ( int(arr_activeElektrode[47]) and int(arr_activeElektrode[48]) and int(arr_activeElektrode[57]) and int(arr_activeElektrode[58]) and int(arr_activeElektrode[62]))==1:
    print(numToBADict[14])
if ( int(arr_activeElektrode[17]) and int(arr_activeElektrode[18]) and int(arr_activeElektrode[28]) and int(arr_activeElektrode[40]) and int(arr_activeElektrode[46]))==1:
    print(numToBADict[15])
if ( int(arr_activeElektrode[18]) and int(arr_activeElektrode[28]) and int(arr_activeElektrode[40]) and int(arr_activeElektrode[46]) and int(arr_activeElektrode[47]))==1:
    print(numToBADict[16])
if ( int(arr_activeElektrode[18]) and int(arr_activeElektrode[28]) and int(arr_activeElektrode[30]) and int(arr_activeElektrode[40]) and int(arr_activeElektrode[41]))==1:
    print(numToBADict[17])
if ( int(arr_activeElektrode[43]) and int(arr_activeElektrode[49]) and int(arr_activeElektrode[50]) and int(arr_activeElektrode[51]) and int(arr_activeElektrode[59]))==1:
    print(numToBADict[18])
if ( int(arr_activeElektrode[5]) and int(arr_activeElektrode[10]) and int(arr_activeElektrode[11]) and int(arr_activeElektrode[12]) and int(arr_activeElektrode[13]))==1:
    print(numToBADict[19])
if ( int(arr_activeElektrode[42]) and int(arr_activeElektrode[43]) and int(arr_activeElektrode[44]) and int(arr_activeElektrode[50]) and int(arr_activeElektrode[51]))==1:
    print(numToBADict[20])
if ( int(arr_activeElektrode[4]) and int(arr_activeElektrode[5]) and int(arr_activeElektrode[10]) and int(arr_activeElektrode[11]) and int(arr_activeElektrode[12]))==1:
    print(numToBADict[21])
if ( int(arr_activeElektrode[40]) and int(arr_activeElektrode[46]) and int(arr_activeElektrode[47]) and int(arr_activeElektrode[48]) and int(arr_activeElektrode[57]))==1:
    print(numToBADict[22])
if ( int(arr_activeElektrode[8]) and int(arr_activeElektrode[9]) and int(arr_activeElektrode[17]) and int(arr_activeElektrode[18]) and int(arr_activeElektrode[28]))==1:
    print(numToBADict[23])
if ( int(arr_activeElektrode[41]) and int(arr_activeElektrode[47]) and int(arr_activeElektrode[48]) and int(arr_activeElektrode[49]) and int(arr_activeElektrode[58]))==1:
    print(numToBADict[24])
if ( int(arr_activeElektrode[30]) and int(arr_activeElektrode[31]) and int(arr_activeElektrode[41]) and int(arr_activeElektrode[42]) and int(arr_activeElektrode[49]))==1:
    print(numToBADict[25])
if ( int(arr_activeElektrode[19]) and int(arr_activeElektrode[28]) and int(arr_activeElektrode[30]) and int(arr_activeElektrode[40]) and int(arr_activeElektrode[41]))==1:
    print(numToBADict[26])
if ( int(arr_activeElektrode[18]) and int(arr_activeElektrode[28]) and int(arr_activeElektrode[30]) and int(arr_activeElektrode[40]) and int(arr_activeElektrode[41]))==1:
    print(numToBADict[27])
if ( int(arr_activeElektrode[8]) and int(arr_activeElektrode[9]) and int(arr_activeElektrode[10]) and int(arr_activeElektrode[18]) and int(arr_activeElektrode[19]))==1:
    print(numToBADict[28])
if ( int(arr_activeElektrode[3]) and int(arr_activeElektrode[8]) and int(arr_activeElektrode[9]) and int(arr_activeElektrode[18]) and int(arr_activeElektrode[19]))==1:
    print(numToBADict[29])
if ( int(arr_activeElektrode[3]) and int(arr_activeElektrode[4]) and int(arr_activeElektrode[8]) and int(arr_activeElektrode[9]) and int(arr_activeElektrode[10]))==1:
    print(numToBADict[30])
if ( int(arr_activeElektrode[3]) and int(arr_activeElektrode[8]) and int(arr_activeElektrode[9]) and int(arr_activeElektrode[17]) and int(arr_activeElektrode[18]))==1:
    print(numToBADict[31])
if ( int(arr_activeElektrode[23]) and int(arr_activeElektrode[34]) and int(arr_activeElektrode[35]) and int(arr_activeElektrode[37]) and int(arr_activeElektrode[38]))==1:
    print(numToBADict[32])
if ( int(arr_activeElektrode[24]) and int(arr_activeElektrode[34]) and int(arr_activeElektrode[35]) and int(arr_activeElektrode[37]) and int(arr_activeElektrode[38]))==1:
    print(numToBADict[33])
if ( int(arr_activeElektrode[24]) and int(arr_activeElektrode[35]) and int(arr_activeElektrode[36]) and int(arr_activeElektrode[38]) and int(arr_activeElektrode[39]))==1:
    print(numToBADict[34])
if ( int(arr_activeElektrode[23]) and int(arr_activeElektrode[24]) and int(arr_activeElektrode[34]) and int(arr_activeElektrode[35]) and int(arr_activeElektrode[36]))==1:
    print(numToBADict[35])
if ( int(arr_activeElektrode[34]) and int(arr_activeElektrode[35]) and int(arr_activeElektrode[37]) and int(arr_activeElektrode[38]) and int(arr_activeElektrode[44]))==1:
    print(numToBADict[36])
if ( int(arr_activeElektrode[13]) and int(arr_activeElektrode[14]) and int(arr_activeElektrode[23]) and int(arr_activeElektrode[24]) and int(arr_activeElektrode[35]))==1:
    print(numToBADict[37])
if ( int(arr_activeElektrode[37]) and int(arr_activeElektrode[44]) and int(arr_activeElektrode[51]) and int(arr_activeElektrode[52]) and int(arr_activeElektrode[53]))==1:
    print(numToBADict[38])
if ( int(arr_activeElektrode[6]) and int(arr_activeElektrode[12]) and int(arr_activeElektrode[13]) and int(arr_activeElektrode[14]) and int(arr_activeElektrode[15]))==1:
    print(numToBADict[39])
if ( int(arr_activeElektrode[2]) and int(arr_activeElektrode[5]) and int(arr_activeElektrode[6]) and int(arr_activeElektrode[7]) and int(arr_activeElektrode[14]))==1:
    print(numToBADict[40])
if ( int(arr_activeElektrode[1]) and int(arr_activeElektrode[2]) and int(arr_activeElektrode[6]) and int(arr_activeElektrode[7]) and int(arr_activeElektrode[16]))==1:
    print(numToBADict[41])
if ( int(arr_activeElektrode[0]) and int(arr_activeElektrode[1]) and int(arr_activeElektrode[2]) and int(arr_activeElektrode[7]) and int(arr_activeElektrode[16]))==1:
    print(numToBADict[42])
if ( int(arr_activeElektrode[59]) and int(arr_activeElektrode[60]) and int(arr_activeElektrode[62]) and int(arr_activeElektrode[63]) and int(arr_activeElektrode[64]))==1:
    print(numToBADict[43])
if ( int(arr_activeElektrode[59]) and int(arr_activeElektrode[60]) and int(arr_activeElektrode[61]) and int(arr_activeElektrode[63]) and int(arr_activeElektrode[64]))==1:
    print(numToBADict[44])
if ( int(arr_activeElektrode[53]) and int(arr_activeElektrode[54]) and int(arr_activeElektrode[60]) and int(arr_activeElektrode[61]) and int(arr_activeElektrode[64]))==1:
    print(numToBADict[45])
if ( int(arr_activeElektrode[26]) and int(arr_activeElektrode[27]) and int(arr_activeElektrode[29]) and int(arr_activeElektrode[45]) and int(arr_activeElektrode[56]))==1:
    print(numToBADict[46])
if ( int(arr_activeElektrode[26]) and int(arr_activeElektrode[27]) and int(arr_activeElektrode[29]) and int(arr_activeElektrode[36]) and int(arr_activeElektrode[45]))==1:
    print(numToBADict[47])
if ( int(arr_activeElektrode[26]) and int(arr_activeElektrode[29]) and int(arr_activeElektrode[36]) and int(arr_activeElektrode[39]) and int(arr_activeElektrode[45]))==1:
    print(numToBADict[48])
if ( int(arr_activeElektrode[37]) and int(arr_activeElektrode[50]) and int(arr_activeElektrode[51]) and int(arr_activeElektrode[52]) and int(arr_activeElektrode[59]))==1:
    print(numToBADict[49])
if ( int(arr_activeElektrode[5]) and int(arr_activeElektrode[11]) and int(arr_activeElektrode[12]) and int(arr_activeElektrode[13]) and int(arr_activeElektrode[14]))==1:
    print(numToBADict[50])
if ( int(arr_activeElektrode[37]) and int(arr_activeElektrode[44]) and int(arr_activeElektrode[51]) and int(arr_activeElektrode[52]) and int(arr_activeElektrode[59]))==1:
    print(numToBADict[51])
if ( int(arr_activeElektrode[1]) and int(arr_activeElektrode[5]) and int(arr_activeElektrode[6]) and int(arr_activeElektrode[12]) and int(arr_activeElektrode[13]))==1:
    print(numToBADict[52])
if ( int(arr_activeElektrode[45]) and int(arr_activeElektrode[54]) and int(arr_activeElektrode[55]) and int(arr_activeElektrode[56]) and int(arr_activeElektrode[61]))==1:
    print(numToBADict[53])
if ( int(arr_activeElektrode[15]) and int(arr_activeElektrode[16]) and int(arr_activeElektrode[26]) and int(arr_activeElektrode[27]) and int(arr_activeElektrode[29]))==1:
    print(numToBADict[54])
if ( int(arr_activeElektrode[53]) and int(arr_activeElektrode[54]) and int(arr_activeElektrode[55]) and int(arr_activeElektrode[60]) and int(arr_activeElektrode[61]))==1:
    print(numToBADict[55])
if ( int(arr_activeElektrode[35]) and int(arr_activeElektrode[36]) and int(arr_activeElektrode[38]) and int(arr_activeElektrode[39]) and int(arr_activeElektrode[53]))==1:
    print(numToBADict[56])
if ( int(arr_activeElektrode[26]) and int(arr_activeElektrode[29]) and int(arr_activeElektrode[36]) and int(arr_activeElektrode[39]) and int(arr_activeElektrode[45]))==1:
    print(numToBADict[57])
if ( int(arr_activeElektrode[25]) and int(arr_activeElektrode[29]) and int(arr_activeElektrode[36]) and int(arr_activeElektrode[39]) and int(arr_activeElektrode[45]))==1:
    print(numToBADict[58])
if ( int(arr_activeElektrode[15]) and int(arr_activeElektrode[16]) and int(arr_activeElektrode[24]) and int(arr_activeElektrode[25]) and int(arr_activeElektrode[26]))==1:
    print(numToBADict[59])
if ( int(arr_activeElektrode[6]) and int(arr_activeElektrode[7]) and int(arr_activeElektrode[15]) and int(arr_activeElektrode[16]) and int(arr_activeElektrode[26]))==1:
    print(numToBADict[60])
if ( int(arr_activeElektrode[6]) and int(arr_activeElektrode[7]) and int(arr_activeElektrode[14]) and int(arr_activeElektrode[15]) and int(arr_activeElektrode[16]))==1:
    print(numToBADict[61])
if ( int(arr_activeElektrode[7]) and int(arr_activeElektrode[15]) and int(arr_activeElektrode[16]) and int(arr_activeElektrode[26]) and int(arr_activeElektrode[27]))==1:
    print(numToBADict[62])

        
        