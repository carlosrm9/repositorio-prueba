import sys
import json
import casatasks as ct
import casaplotms as cplot

def handle(req):

    params = json.loads(req)

    ct.flagdata(**params)

    print('Function run succesfully!')