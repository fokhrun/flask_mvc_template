
## create a venv

python -m venv app-env

in windows:
activate by app-env\scripts\activate
deactivate by deactivate


## Add debugger
Debugging a Flask app in VSCode involves setting up a launch configuration. 
Here's an example configuration for debugging a Flask app in VSCode:

- Open your Flask project in VSCode.
- Create a launch.json file inside the .vscode directory in your project if it doesn't exist.
- VsCode will auto generate the launch.json if you provide correct options, for example python, then Python: Flask, and wsgi.py


"""
    {
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "wsgi.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
"""


- Set breakpoints in your code by clicking in the gutter area next to the line number in VSCode.

- Start the debugger by pressing F5 or clicking on the debug icon in VSCode and selecting the Flask configuration you just created.

- This setup will allow you to debug your Flask app by running it in debug mode within VSCode.
