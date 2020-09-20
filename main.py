import gzip
import os
import sys


def convert(path):
    if not path.endswith("/"):
        path += "/"
    for item in os.listdir(path):
        if item.endswith(".gz") or os.path.isdir(path + item):
            continue
        else:
            item_path = path + item
            with open(item_path, "r") as read_file:
                data = bytearray(read_file.read(), encoding="UTF-8")
            with gzip.open(item_path + ".gz", "w") as write_file:
                write_file.write(data)
            os.remove(item_path)


def main():
    if not len(sys.argv) == 2:
        sys.stderr.write("Usage: main.py <path-to-directory>") 
        return
    convert(sys.argv[1])


if __name__ == "__main__":
    main()
