# do
A simple Download Organizer

## Installation
Clone the repository:
```
git clone https://github.com/adi-075/do
cd do
```

Install the required packages
```
pip install -e . 
```

## Usage
Organize your Downloads folder

```sh
python main.py -h
usage: main.py [options] [directory]

```

## Project Structure
```
do/                          
├── organizer/                
│   ├── __init__.py            
│   ├── file_organizer.py      # File organizing logic
│   └── config.py              # Configure the Folder and the extensions 
├── test/                     
│   ├── __init__.py            
│   └── test_organizer.py      # Unit tests for the file organizer
├── pyproject.toml             
├── main.py                    # Main function ( Call this )
├── README.md                  
├── .gitignore                
└── LICENSE
```

- The config.py file sets up categories to sort your files
- You can define your own categories in this file
