import os
import sys


sys.path.append(".") 

NO_PATH = sys.maxsize

from floyd.floyd_rec import Floyd
from floyd.floyd_imp import floyd
from test_cases import (input_a, input_b, input_c, input_d)

import cProfile
testcode = '''
path = []
for n in input_a:
    for n in input_b:
        for n in input_c:
            for n in input_d:
                path.append(())
'''

if __name__ == '__main__':
    cProfile.run("floyd(input_a)")
    cProfile.run("floyd(input_b)")
    cProfile.run("floyd(input_c)")
    cProfile.run("floyd(input_d)")
