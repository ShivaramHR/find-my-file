# PyFind

PyFind is a command-line file search tool written in Python.  
It recursively searches through directories and allows filtering files based on name patterns, extensions, file contents, and file size.

This project demonstrates directory traversal, file inspection, and command-line argument handling using Python's standard library.

---

## Features

- Recursively traverses directories
- Lists all files inside a given folder
- Search files by filename pattern
- Search files by extension
- Search files containing specific text
- Search files by minimum file size
- Simple command-line interface
- No external dependencies

---

## Project Structure

```
find-my-file/
│
├── pyfind.py
├── projects/
└── README.md
```

---

## Usage

Run the script from the terminal and provide the directory you want to search.

```
python3 pyfind.py <directory>
```

### Example

```
python3 pyfind.py projects
```

Example output:

```
/Users/username/find-my-file/projects/hello.py
/Users/username/find-my-file/projects/findSum/sum.py
```

---

## Search by Filename Pattern

Search files using wildcard patterns.

```
python3 pyfind.py projects --name "*.py"
```

Example output:

```
/Users/username/find-my-file/projects/hello.py
/Users/username/find-my-file/projects/findSum/sum.py
```

---

## Search by File Extension

```
python3 pyfind.py projects --ext py
```

Example output:

```
/Users/username/find-my-file/projects/hello.py
/Users/username/find-my-file/projects/findSum/sum.py
```

---

## Search by File Contents

Find files that contain specific text.

```
python3 pyfind.py projects --content "import"
```

Example output:

```
/Users/username/find-my-file/projects/hello.py
/Users/username/find-my-file/projects/findSum/sum.py
```

---

## Search by File Size

Find files larger than a given size (in bytes).

```
python3 pyfind.py projects --size 1000
```

Example output:

```
/Users/username/find-my-file/projects/largefile.txt
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## Learning Goals

This project was built to practice:

- File system traversal with `os.walk`
- Command-line argument parsing using `sys.argv`
- Pattern matching with `fnmatch`
- File content scanning
- File size inspection
- Designing modular CLI tools

---

## Future Improvements

Possible enhancements:

- Combine multiple filters (e.g. extension + content)
- Add `--ignore` to skip directories
- Add file modification date filtering
- Support human-readable size formats (`10KB`, `5MB`)
- Add CLI help output (`--help`)

---

## License

MIT License