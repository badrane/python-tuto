# verification d'un numero SS

import re

regex = r"\A[12][0-9]{2}[0-1][0-9](2[AB]|[0-9]{2})[0-9]{3}[0-9]{3}"

test_str = "3570575358004"

prog = re.compile(regex)
result = prog.match(test_str)
if result is not None:
    print("ok\n")
else:
    print("wrong SS number\n")