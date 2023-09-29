# DSCLI Python

DSCLI Python is a Python wrapper for the `dscli` command-line tool, designed to interact with various data structures and retrieve relevant information. It utilizes the `pexpect` library to automate interactions with the `dscli` command-line tool.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Credits](#credits)
- [License](#license)

## Description

The DSCLI Python Interface simplifies the process of running `dscli` commands and fetching alarms by providing a Pythonic interface. It allows users to interact with `dscli` in a programmatic way, making it easier to automate tasks and integrate with other Python projects.

The key features of this project include:

- **Automated Interaction**: The interface automates the interaction with the `dscli` command-line tool, including sending commands and capturing output.

- **Alarms Retrieval**: One of the main functionalities is to run a `dscli` session and retrieve a number of alarms.

## Installation

To use DSCLI Python, follow these installation steps:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/dscli-python-interface.git
```
2. Change to the project directory:
```bash
cd dscli-python/dscli
```
3. Install the necessary dependencies:
```bash
pip install six
pip install pexcept
```
4. Execute DSCLI
```bash
python dscli.py
```

## Credits

**Author**: Taylor C. Richberger <taywee@gmx.com>

## License

This project is licensed under the MIT License - see the **LICENSE** file for details.
