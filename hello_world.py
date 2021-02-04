#!/usr/bin/env python    # 1

import sys          #  2
v = sys.version_info   # 3
print(v)     # 4
version = ".".join(str(x) for x in v)  # 5
print(version)   # 6
print ("hello python (version " + version + " )" )  # 7
