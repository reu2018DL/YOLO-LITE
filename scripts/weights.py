import os
import numpy as np
import sys


class weights_walker(object):
    """incremental reader of float32 binary files"""
    def __init__(self, path):
        self.eof = False # end of file
        self.path = path  # current pos
        if path is None:
            self.eof = True
            return
        else:
            self.size = os.path.getsize(path)# save the path
            major, minor, revision, seen = np.memmap(path,
                shape = (), mode = 'readwrite', offset = 0,
                dtype = '({})i4,'.format(4))
            self.transpose = major > 1000 or minor > 1000
            self.offset = 0

    def walk(self, size):
        if self.eof: return None
        end_point = self.offset + 4 * size
        assert end_point <= self.size, \
        'Over-read {}'.format(self.path)

        float32_1D_array = np.memmap(
            self.path, shape = (), mode = 'readwrite',
            offset = self.offset,
            dtype='({})float32,'.format(size)
        )

        self.offset = end_point
        if end_point == self.size:
            self.eof = True
        return float32_1D_array






## USAGE python weights.py NAMEOFWEIGHTSFILE THRESHOLD
if __name__ == '__main__':
    argv    = sys.argv
    inName  = argv[1]
    thresh  = float(argv[2])
    print(thresh)
    walker  = weights_walker(inName)
    totalRead= int((walker.size - walker.offset)/4)
    data     = walker.walk(totalRead)
    # data.tofile(open(oldName,"w"))
    data[np.abs(data)<thresh] = 0
