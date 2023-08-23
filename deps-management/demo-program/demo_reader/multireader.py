
import os

from demo_reader.compressed import bzipped, gzipped

extension_map = {
    '.bz2' : bzipped.opener,
    '.gz': gzipped.opener   
}

class MultiReader:
    def __init__(self, filename) -> None:
        # self.filename = filename
        # self.f = open(filename, 'rt')

        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, 'rt')
    
    def close(self):
        self.f.close()
    
    def read(self):
        return self.f.read()