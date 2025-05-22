# Commands for installing/updating using PIP
# Python Package Index: https://pypi.org/

# WARNING WARNING WARNING
# PARENT FILE/FOLDER STRUCTURE MUST NOT HAVE SPECIAL CHARACTERS OR SPACES
# INSTALLS AND IMPORTS FOR THE VIRTUAL ENVIRONMENT WILL NOT WORK.

# --------- Install a module ---------
# py -m pip install module
# Example:
# py -m pip install requests

# --------- List all modules currently installed ---------
# py -m pip list = List all installed modules.
# pip list can also be used to list modules.

# --------- Install a specific version of a module ---------
# py -m install module==versionnumber
# Example:
# py -m install requests==2.30.0

# --------- Update a module ---------
# py -m pip install --upgrade module
# Example:
# py -m pip install --upgrade requests

# --------- View information about a module ---------
# py -m pip show module
# Will show details regarding the module.

# --------- Freeze requirements to a .txt file ---------
# py -m pip freeze > requirements.txt
# Will list all requirements/dependencies for the project.

# Packages to install for the virtual environment

# py -m pip install requests (Python HTTP for Humans.)
# py -m pip install python-dotenv (Read key-value pairs from a .env file and set them as environment variables )

# Commands for Virtual Environments

# --------- Creating a virtual environment ---------
# py -m venv .venv

# --------- Activate a virtual environment ---------
# source .venv/Scripts/activate
# Will start your virtual environment. Will see your
# virtual environment as (.venv) above your terminal block.
# Need to activate each time you work on the project.

# --------- Deactivate the current virtual environment ---------
# deactivate
# This brings you back to your global environment

# Use pip list to view all installed modules in your virtual environment.
