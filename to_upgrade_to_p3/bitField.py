#! /usr/bin/env python
#
# bitfield manipulation
#
# based on code from http://code.activestate.com/recipes/113799/
#


class bf(object):
    def __init__(self,value=0,length=0):
        if length:
            self._mask = 2**(length)-1
        else:
            self._mask = ~0
        self._length=length
        self._d = value & self._mask

    def __len__(self,):
        return (self._length)

    def __str__(self,):
        if self._length :
            return (("{:0"+str(self._length)+"b}").format(self._d))
        else:
            return ("{:b}".format(self._d))

    def __getitem__(self, index):
        return (self._d >> index) & 1

    def __lshift__(self, index):
        return bf((self._d << index) & self._mask,self._length)

    def __rshift__(self, index):
        return bf((self._d >> index) & self._mask,self._length)

    def __and__(self, other):
        return bf((self._d & other) & self._mask,self._length)

    def __or__(self, other):
        return bf((self._d | other & self._mask),self._length)

    def __xor__(self, other):
        return bf((self._d ^ other & self._mask),self._length)

    def __bool__(self):
        return (self._d != 0)

    def __invert__(self):
        return bf((  ~self._d& self._mask),self._length)


    def __lt__(self, other):
        return (int(self._d) <  int(other))

    def __le__(self, other):
        return (int(self._d) <=  int(other))

    def __eq__(self, other):
        return (int(self._d) ==  int(other))

    def __ne__(self, other):
        return (int(self._d) !=  int(other))

    def __gt__(self, other):
        return (int(self._d) >  int(other))

    def __ge__(self, other):
        return (int(self._d) >=  int(other))

    def __setitem__(self,index,value):
        value    = (value&1)<<index
        mask     = (1)<<index
        self._d  = (self._d & ~mask) | value

    def __getslice__(self, start, end):
        mask = 2**(end - start) -1
        return (self._d >> start) & mask

    def __setslice__(self, start, end, value):
        mask = 2**(end - start) -1
        value = (value & mask) << start
        mask = mask << start
        self._d = (self._d & ~mask) | value
        return (self._d >> start) & mask

    def __int__(self):
        return self._d  & self._mask # should never need the & mask here, but just to be sure..

# ByteToHex From http://code.activestate.com/recipes/510399-byte-to-hex-and-hex-to-byte-string-conversion/

def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """

    hex = []
    for aChar in byteStr:
        hex.append( "%02X " % aChar )

    return ''.join( hex ).strip()

if __name__ == "__main__":

    k = bf()
    k[3:7]=5
    print("{:04x}".format(int(k)))
    k[3:7]=15
    print("{:04x}".format(int(k)))
    k = bf()
    k=bf(31)
    print("{:04x}".format(int(k)))

    print(k[3])
    print(k[5])
    k[7]=1
    print(k[4:8])
    print(int(k))

    k = bf(0xFFFF)
    k[4:8]=0x0
    print("{:04x}".format(int(k)))

