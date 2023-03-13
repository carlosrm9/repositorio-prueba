# Copyright (c) Alex Ellis 2017. All rights reserved.
# Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import sys
import sys
import json
import casatasks as ct
import casaplotms as cplot

def handle(req):

    params = json.loads(req)

    ct.flagdata(**params)

    print('Function run succesfully!')

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if __name__ == "__main__":
    st = get_stdin()
    ret = handle(st)
    if ret != None:
        print(ret)
