# do
A simple Download Organizer

## Installation
Clone the repository:
```sh
https://github.com/adi-075/do
cd do
```

Install the required packages
```
pip install -e . 
```

## Usage
Organize your Downloads folder

```py
python main.py -h
usage: main.py [options] [directory]

Organize files in your Downloads folder with do.

positional arguments:
  directory   The directory to organize. Defaults to the Downloads folder

options:
  -h, --help  show this help message and exit
```

- The config.py file sets up categories to sort your files
- You can define your own categories in this file
