import os
import sys
import fnmatch


def getFilePath(dir):
    for root, _, files in os.walk(dir):
        for file in files:
            if file.startswith("._"):
                continue
            print(os.path.join(root, file))

def searchFilePattern(dir, pattern):
    sameFileTypes = []
    for root, _, files in os.walk(dir):
        for file in files:
            if file.startswith("._"):
                continue
            if fnmatch.fnmatch(file, pattern):
                sameFileTypes.append(os.path.join(root, file))
    return sameFileTypes

def searchFileExtension(dir, extension):
    return searchFilePattern(dir, f"*.{extension}")


def execute():
    if len(sys.argv) == 1:
        print("No arguments provided")
        sys.exit(1)
    currDir = os.getcwd()
    if '.' not in sys.argv[1] and len(sys.argv) == 2:
        fileName = sys.argv[1]
        newDir = os.path.join(currDir, fileName)
        getFilePath(newDir)

    fileName = sys.argv[sys.argv.index('.')-1]
    newDir = os.path.join(currDir, fileName)


    if "--name" in sys.argv:
        pattern = sys.argv[sys.argv.index("--name") + 1]
        sameFileTypes = searchFilePattern(newDir, pattern)
        for ele in sameFileTypes:
            print(ele)
    if "--ext" in sys.argv:
        extension = sys.argv[sys.argv.index('--ext') +1]
        sameFileExt = searchFileExtension(newDir, extension)
        for ele in sameFileExt:
            print(ele)


if __name__ == "__main__": 
    execute()