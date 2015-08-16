from PIL import Image
from glob import glob

print("I am also imported")

def getReport(ext, path):
    for fname in glob("*." + ext):
        try:
            alpha = Image.open(fname)
            w, h = alpha.size
            yield 'image: "{}", width: {}, height: {}'.format(fname, w, h)
        except IOError:
            pass
        finally:
            try:
                alpha.close()
            except Exception:
                pass
