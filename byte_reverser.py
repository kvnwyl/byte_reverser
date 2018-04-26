import sys

class byte_reverser:
    """Class file to read in files from command line arguments and
    reverse the bytes in each file
    """
    def __init__(self):
        system_args = sys.argv[1:]
        if len(system_args) < 1:
            self.usage_information()
        else:
            for arg in system_args:
                self.file_name = arg
                self.file_extension = arg.split(".")[-1]
                self.file_data = None

                self.read_file()
                self.write_file()

    def read_file(self):
        try:
            with open(self.file_name, "rb") as f:
                self.file_data = f.read()
        except:
            print("Unable to open source document")
            return

    def write_file(self):
        file_name = "{0}_reversed.{1}".format(self.file_name.replace(self.file_extension, "")[:-1], self.file_extension)
        try:
            with open(file_name, "wb") as f:
                f.write(self.file_data[::-1])
        except:
            print("Unable to write destination document")
            return

    def usage_information(self):
        print("Usage Information: byte_reverser.py <Files To Reverse>...")

x = byte_reverser()