class flatSet(object):
    count = 3
    bin = 2
    filter = ["u-band","g-band","r-band","etc"]
    #u-band, g-band, r-band, i-band, z-band, clear, or h-alpha

    def __init__(self, bin, filter, count):
        #assign the class attributes
        self.bin = bin
        self.filter = filter
        self.count = count
