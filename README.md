# Spice Magic

[Spice Magic](https://restaurant-binita-99be9591d7d4.herokuapp.com/) is a full stack restaurant website. The site provides 
- the site guests to see the restaurant menu
- the site owner to manage reservations for its restaurant guests through a centrally managed reservation database
- The site provides a role-based management of reservation database

# Requirements

## Functional requirements

The site supports three types of users:
- `visitor`: can visit publicly available pages, anyone who landed in the site
- `guest`: can reserve tables in the restaurant on his own
- `admin`: 
    - can create reservation slots 
    - can cancel anyone's reservation (to handle unforeseeable situations)
    - can book reservation on behalf of any restaurant customer (offline booking)

The site has the following pages: 
1. `home`: provides information about the restaurant, such as cousine, menu, serving hours, contact, etc., for any site visitors
2. `registration`: registration for new guest users
3. `login`: login for both `guest` and `admin` users
    a. any user can log in using his credentials
    b. `user` who cannot be authenticated are redirected to the login page with an error message 
4. `reserve`: 
    1. `guest` can 
        - view available reservations within the next two weeks from today 
        - can see his resevations 
        - make reservations for any available time for any number of guests within the next two weeks from today
            - can add a remark about reservations
        - cancel already made reservations
        - cannot reserve table reserved by someone else

    2. `admin` can 
        - view any reservations status of any table made by anyone
        - make reservations for anyone
            - can add a remark about reservations
        - cancel anyone's reservation
    3. `reservation_admin` can
        - create new type of tables 
        - remove any existing type of tables
        - create any new reservation slot
        - remove any existing reservation slot

## Technical Requirements
- The site should be a full-stack website that is inspired by MVC framework with the following tech stack
    - Frontend implemented by HTML, CSS, and Javascript
    - Backend implemented by Python web frameworks
    - Database
- It implement application features and business logic to manage, query and manipulate data to handle reservetion information stored in the chosen database platform using an ORM tool that goes with the chosen Python framework
    - The Python code should be Written consistently using the PEP8 style guide
    - The Python code should handle the bulk of the business logic
    - Adopt an MVC like design where models, views, and controllers are isolated for flexible manipulation
    - Automated tests should be written for bulk of the Python code
- The front-end meets a good accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions
    - Implement forms with validations to create and edit models in the backend
- It implements identification and apply authorisation, authentication and permission for users to handle reservations
    - Apply role-based login and registration functionality
    - The current login state is reflected to the user
    - Users should not be permitted to access restricted content or functionality prior to role-based login
- The site should stay reliable to changes in the code leveraging manual and automated tests
    - Test procedures should assess functionality, usability, responsiveness, and data management within the entire web application
    - Automated tests should be written for both Python and Javascript
- The code should be free of any passwords or security-sensitive information to the repository and the hosting platform
- The site should be deployed to Heroku


## Software Project Management Requirements
- The planning and delivery progress should be managed using GitHub issues
- The user stories implemented by the site should be documented as GitHub Issues
- Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc., created as part of the design process and its reasoning
- It codebase should be managed using GitHub repository so that a team of software develop can contribute without conflicts at the same time
- The HTML and CSS code should be validated
- The codebase should be readable and leverage a good balance of comments, indentation, consistent and meaningful naming conventions for files, modules, functions, and other code components


# Tecnical Design

## High-level tech stack

- Front End: [Bootstrap Framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/) (HTML, CSS, Javascript)
- Back End: [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/) (Python)
    - ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Database: [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)
- Cloud: [Heroku](https://dashboard.heroku.com/apps)

## High-level architecture

![High-level application architecture](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/data_model.png)

### Controllers

## Data model

![Data Model](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/flask_app_architecture.png)

### Code repository structure
```
- app/ : source code for the flask app
    - __init__.py : include app factory method where blueprints, migration handler, database handler, login manager, etc., are registered
    - models.py : include data models used in the app to interact with the database
    - main/ : placeholder for main routes /, /reserve, and /admin
        - __init__.py : define the /main blueprint (for /, /reserve, /admin routes)
        - forms.py : form objects to interact with forms in the front end
        - views.py : route handlers (controller part of MVC) for /, /reserve, and /admin 
        - errors.py : error handlers, such as 404, 500, etc.
        - *.py : other helper modules to support route handlers in views.py
    - auth/ : placeholder for auth routes /login
        - __init__.py : define the /auth blueprint ()
        - view.py
    - templates/
        - *.html : views to be rendered in the site
    - static/ : images to be rendered in the site
- migrations/ : database migration scripts
- tests/ : unit tests
    - main/ : tests for app/main
    - auth/ : tests for app/auth
    - test*.py : tests for files in app/
- docs/ : deep dive documentations
- venv/ : virtual environment for the local development, should not be tracked by git
- .env/ : key information to work with the flask app and local MySQL database
- .gitignore : files and foldered to be ignored, such venv, .env
- LICENSE : source code usage and copy license
- Procfile : app run command to be used in the heroko production environment
- runtime.txt : Python runtime to be used in the heroku production environment
- requirements.txt : Python library (and its version) to be used development, testing, and production environment
- config.py : configuration for flask and MySQL in development, testing, and production environment
- wsgi.py : main entry point to run the app through command line
```

## Special techniques

### Flask app factory

Typically a flask app is created in a single-file version advocated by many sources. Such an application is created in the global scope, there is no way to apply configuration changes dynamically. So it is too late to make configuration changes, which can be important for unit tests. We deal with this problem we delay the creation of the application by moving it into a factory function that can be explicitly invoked from the script. This not only gives the script time to set the configuration, but also the ability 
to create multiple application instances—another thing that can be very useful during testing.

Check `app\__init__.py` for more details.

### Password management

### Current user

## Future improvements

### Model
- must
    - User
        - validation for `email` to be actual email address
- should
    - User
        - make `role` non-nullable
- could
    - User

    -   

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

### Test cases



