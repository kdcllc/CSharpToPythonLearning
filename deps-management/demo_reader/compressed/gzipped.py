import gzip

# refactored code
#import sys

from ..util import writer

opener = gzip.open

if __name__ == '__main__':
    # refactored code
    # f = gzip.open(sys.argv[1], mode='wt')
    # f.write(' '.join(sys.argv[2:]))
    # f.close()

    writer.main(opener)