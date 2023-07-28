#!/bin/bash
THIS_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

RED='\033[0;31m'
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

function echo {
    #last arg is string
    STRING=${@: -1}
    #all but last args are colors or other options
    OPTIONS=${@:1:$#-1}
    builtin echo -e $OPTIONS "$STRING" $NC
}

echo "${CYAN}Welcome to the pyhelp installer script!${NC}"
echo "${CYAN}This script will install pyhelp and its dependencies.${NC}"

echo "${CYAN}Checking for python3...${NC}"
# check if python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "${RED}Python3 is not installed.${NC}"
    # check if apt is available
    if ! command -v apt &>/dev/null; then
        echo "${RED}apt is not available. Please install python3 and try again.${NC}"
        exit 1
    fi
    #prompt to try installing python3
    read -p "Do you want to try installing python3? [y/n]: " install_python3
    if [ "$install_python3" == "y" ]; then
        echo "${CYAN}Installing python3...${NC}"
        apt install python3 >/dev/null 2>&1
        echo "${GREEN}python3 is installed.${NC}"
    else
        exit 1
    fi
fi
echo "${GREEN}python3 is installed.${NC}"

# install requirements
echo "${CYAN}Installing requirements...${NC}"

REQUIREMENTS_FILE="$THIS_SCRIPT_DIR/requirements.txt"
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "${RED}requirements.txt file not found.${NC}"
    # prompt for path
    read -p "Enter path to requirements.txt file: " REQUIREMENTS_FILE
    # check if file exists
    if [ ! -f "$REQUIREMENTS_FILE" ]; then
        echo "${RED}requirements.txt file not found.${NC}"
        exit 1
    fi
fi

python3 -m pip install -r "$REQUIREMENTS_FILE"
echo "${GREEN}Requirements installed.${NC}"

# install pyhelp
echo "${CYAN}Installing pyhelp...${NC}"

# determine the correct path to install pyhelp
PATH="/usr/local/bin/pyhelp"
# check folder
FOLDER="/usr/local/bin"
if [ ! -d "$FOLDER" ]; then
    echo "${RED}$FOLDER does not exist.${NC}"
    # prompt for path
    read -p "Enter path to install pyhelp: " PATH
    # check if folder exists
    if [ ! -d "$PATH" ]; then
        echo "${RED}$PATH does not exist.${NC}"
        exit 1
    fi
fi
# check if pyhelp is already installed
if [ -d "$PATH" ]; then
    echo "${RED}pyhelp is already installed.${NC}"
    # prompt to reinstall
    read -p "Do you want to reinstall pyhelp? [y/n]: " reinstall_pyhelp
    if [ "$reinstall_pyhelp" == "y" ]; then
        echo "${CYAN}Removing old pyhelp...${NC}"
        rm -rf "$PATH" >/dev/null 2>&1
        echo "${GREEN}Old pyhelp removed.${NC}"
    else
        exit 1
    fi
fi

# copy pyhelp to install path
echo "${CYAN}Copying pyhelp to $PATH...${NC}"
/bin/cp -r "$THIS_SCRIPT_DIR/pyhelp.py" "$PATH" >/dev/null 2>&1
echo "${GREEN}pyhelp installed.${NC}"

# chmod pyhelp
echo "${CYAN}Setting permissions for pyhelp...${NC}"
/bin/chmod +x "$PATH" >/dev/null 2>&1
echo "${GREEN}Permissions set.${NC}"

echo "${GREEN}pyhelp is installed!${NC}"
echo "${GREEN}Run pyhelp --help to get started. you might have to restart your terminal first${NC}"
echo "${CYAN}Happy coding!${NC}"
