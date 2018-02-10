import sys

# datos introducidos por teclado
data = sys.argv[:]

print 'data =  ', data

print "% d arguments were passed to the script % s: " \
          % (len(sys.argv) - 1, sys.argv[0])
for arg in sys.argv[1:]:
    print " % s" % arg