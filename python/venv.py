'''VIRTUAL ENVIRONMENT:
        # python -m venv venv
        # pip install virtualenv
            :.virtualenv [directory]
'''
'''pip:
pip install python packages
:.pip uninstall -r requirements.txt
PyPI:
        The Python Package Index
'''

'''
    Poetry:
            Package manager for Python.
            :.manages virtual environment
            :.manages dependencies
            :.can be used to build python packages that we can share with others.
        (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
        #Starting a new project:
                poetry new demo
        #To add a dev dependency, we can add the --dev option to the add command, like so:
                 poetry add --dev <package name>
        #To build a package we can use:
                poetry build
                    :. creates 2 files- .whl(wheel file)
                                        tar.gz file: file containing the package's source code
        #To create an access token:
                poetry config pypi-token.pypi <token>
        
        #To publish our package :
                poetry publish
    Poetry is interoperable:
                Converting an existing project to Poetry:
                                cd my-project
                                poetry init
                Exporting to a regular requirements.txt file:
                                poetry export -f requirements.txt -o requirements.txt
                
'''
'''
poetry --version:	Shows the version of your poetry installation
poetry new <name>:	Create a new poetry project
poetry init:	Start a wizard that helps you convert an existing project to a Poetry project
poetry add <package>:	Add package to pyproject.toml, resolve dependencies, and install the package in the venv
poetry remove <package>:	Remove package from your project (including its dependencies)
poetry show	:List the installed packages
poetry export -o <filename>	:Export the list of dependencies to a requirements.txt file
poetry install: Install all dependencies of the current poetry project. Uses poetry.lock if present.
poetry run <command>:	Run the command inside the project’s virtual environment
poetry shell:	Start a new shell with the project’s virtual environment activated
'''
'''
Issues due to pip:
                Dependency conflicts:
                
                System Breakage:
                
                Difficulty Isolating Issues:
                
                Not easy to remove or update packages:
                
                Lack of isolation:

'''

'''
                pipx:
                        It is a utility for installing and running Python applications in isolated environments.
                        
'''