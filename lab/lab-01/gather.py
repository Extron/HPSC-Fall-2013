#!/usr/bin/env python

from popen import subprocess
import os

trials = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]

with open('data.csv', 'w') as f:
    f.write('key,value')

    for trial in trials:
        p = subprocess.Popen('triad ' + string(trial))
        p.wait()
        out, err = p.communicate()
        report = out.split()
        f.write(report[1], report[3])

        
