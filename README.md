# PyFind

PyFind is a simple command-line file search tool written in Python.  
It recursively searches through directories and prints the full path of all files inside a given folder.

This project demonstrates directory traversal using Python's `os` module and basic command-line argument handling with `sys`.

---

## Features

- Recursively traverses directories
- Lists all files inside a given folder
- Prints full file paths
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


## Requirements

- Python 3.x
- No external libraries required

---

## Future Improvements

Possible enhancements:

- Search files by extension
- Search files by filename pattern
- Search file contents
- Add command-line flags (e.g. `--ext`, `--name`)
- Ignore hidden files and system files

---

## Learning Goals

This project was built to practice:

- File system traversal
- Command-line arguments (`sys.argv`)
- Using Python's `os` module
- Building simple CLI tools

---

## License

MIT License