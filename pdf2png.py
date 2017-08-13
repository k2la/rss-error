import os
import os.path
import fnmatch
import subprocess
import sys

def execute(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, u"*.pdf"):
                org_path = os.path.join(dirpath, filename)
                png_path = org_path.replace(".pdf", ".png")
                print("convert {0} to {1}".format(org_path, png_path))
                if subprocess.call(["convert", "-density", "300", "-trim", org_path, png_path]) != 0:
                    print("failed: {0}".format(org_path))

if __name__ == '__main__':
    root_path = sys.argv[0]
    execute(root_path)