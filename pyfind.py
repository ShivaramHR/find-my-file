import os
import sys
import fnmatch


def getFilePath(dir):
    for root, _, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            if file.startswith("._"):
                continue
            print(path)

def searchFilePattern(dir, pattern):
    sameFileTypes = []
    for root, _, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            if file.startswith("._"):
                continue
            if fnmatch.fnmatch(file, pattern):
                sameFileTypes.append(path)
    return sameFileTypes

def searchFileExtension(dir, extension):
    return searchFilePattern(dir, f"*.{extension}")

def searchFileContents(dir, content):
    sameFileContent = []
    for root, _, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            if file.startswith("._"):
                continue
            try:
                with open(path, 'r', errors='ignore') as f:
                    if content in f.read():
                        sameFileContent.append(path)
            except:
                continue
    return sameFileContent

def searchBySize(dir, size):
    try:
        sizeInBytes = int(size)
        sameFileSize = []
        for root, _, files in os.walk(dir):
            for file in files:
                path = os.path.join(root, file)
                if file.startswith("._"):
                    continue
                try:
                    if os.path.getsize(path) >= sizeInBytes:
                        sameFileSize.append(path)
                except:
                    continue
        return sameFileSize
    except Exception as e:
        print(f"Error: {e}")
        return []


def execute():
    if len(sys.argv) == 1:
        print("No arguments provided")
        sys.exit(1)
    fileName = sys.argv[1]
    newDir = os.path.abspath(fileName)
    if not os.path.isdir(newDir):
        print(f"Error: {newDir} is not a directory")
        sys.exit(1) 

    if len(sys.argv) == 2:
        getFilePath(newDir)
        return

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
    if "--contains" in sys.argv:
        content = sys.argv[sys.argv.index("--contains") + 1]
        sameFileContents = searchFileContents(newDir, content)
        for path in sameFileContents:
            print(path)
    if "--size" in sys.argv:
        size = sys.argv[sys.argv.index("--size") + 1]
        sameFileSize = searchBySize(newDir, size)
        for path in sameFileSize:
            print(path)

if __name__ == "__main__": 
    execute()