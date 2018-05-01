import os
import sys


class ByteReverser:
    """Class file to read in files from command line arguments and
    reverse the bytes in each file
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, "rb") as f:
                return f.read()[::-1]
        except Exception as e:
            print("An error occured while "
                  "opening the file '{}'".format(
                      self.file_name))


if __name__ == "__main__":

    args = sys.argv[1:]

    if not args:
        print("Usage Information: byte_reverser.py <Files To Reverse>...")

    for arg in args:
        file_name = os.path.basename(arg)
        reverser = ByteReverser(file_name)

        with open("reversed_{}".format(file_name), "wb") as target:
            target.write(reverser.read())
