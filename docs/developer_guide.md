
# Developer Guide

## Developer Environment

1. Ensure that you have a Python version at least `Python v3.11` and `pip v23.3.1`
2. Clone the repository https://github.com/fokhrun/restaurant_reservation.git as `restaurant_reservation` in your local directory
3. Work inside `restaurant_reservation`
2. Create a virtual environment using `venv`:
    ```
    1. python3 -m venv venv
    2. .\venv\Scripts\activate
    3. pip install -r .\requirements.txt
    ```
5. Download and install MySQL v8.0.35 or upwards from `https://dev.mysql.com/downloads/installer/`
6. Setup a database `restaurant_dev`
7. Make a copy of `.env_template` as `.env` and fill in the missing valuesg
8. Initialize the database with right tables and their starter values by running `python .\iniatialize_db.py` 
9. Run the app `flask run --debug`
10. You can use `VSCode` as an editor

## Add debugger
Debugging a Flask app in `VSCode` involves setting up a launch configuration. 
Here's an example configuration for debugging a Flask app in VSCode:

- Open your Flask project in `VSCode`
- Create a `launch.json` file inside the `.vscode` directory in your project if it doesn't exist.
- VSCode will auto generate the `launch.json` if you provide correct options, for example python, then Python: Flask, and wsgi.py


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

## Testing

- Add test codes in `tests` folder
- Run `flask test`