import sys

argc = len(sys.argv)
if argc == 2:
    f = sys.stdin
elif argc == 3:
    f = open(sys.argv[2], "rU")
try:
       f = open(sys.argv[2],"rU")
except IOError:
       print >> sys.stderr, "Error: open file"
       sys.exit(1)

line = f.readline()
while line:
    i=1
    print (i + line)
    line = f.readline()
    i = i + 1
f.close
~       

