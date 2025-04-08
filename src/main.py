import sys

if __name__ == "__main__":
    filePath = sys.argv[1]
    file = open(filePath, "r")
    for line in file:
        print(line)
