import sys

def main(opener):
    f = opener(sys.argv[1], mode='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()