# recipeBook

Setting up Python Virtual Environment

Virtual Environment is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.

I use such a virtual environment to work in the same conditions in order to use the same dependencies needed to develop the project.
Installing virtualenv

python -m pip install virtualenv

Creating and activating a virtual environment

    PyCharm

    VS Code - up to the 4th minute

    Creating virtualenv - Windows/Linux, where venv is the name of the environement

    python -m venv venv

    Activating virtualenv - Windows

    .\venv\Scripts\activate

    Activating virtualenv - Linux

    venv/bin/activate

Installing packages

python -m pip install -r requirements.txt

Setting up Flask environement

I use different configurations depending on the environment (development, production, testing) in which the application is running.

    Windows

    set FLASK_APP=run.py
    set FLASK_ENV=development

    Linux

    export FLASK_APP=run.py
    export FLASK_ENV=development 

Starting the app

    Flask CLI

    flask main

    Python

    python main.py
