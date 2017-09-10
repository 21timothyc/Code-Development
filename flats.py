class flatSet(object):
    count = 3
    bin = 2
    filter = "g-band"
    #u-band, g-band, r-band, i-band, z-band, clear, or h-alpha

    def __init__(self, bin, filter, count):
        #assign the class attributes
        self.bin = bin
        self.filter = filter
        self.count = count
    
    def toString(self) -> str:
        return 'This set of flats has a count of %d, binning of %s, and filter is set at %s.'%(self.count, self.bin, self.filter)

fs = flatSet(bin,filter,count)
print(fs.toString())
