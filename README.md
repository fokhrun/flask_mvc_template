# Spice Magic

### Table of contents

- [Overview](https://github.com/fokhrun/restaurant_reservation#Overview)
- [Requirements](https://github.com/fokhrun/restaurant_reservation#requirements)
    - [Functional Requirements](https://github.com/fokhrun/restaurant_reservation#functional-requirements)
    - [Technical Requirements](https://github.com/fokhrun/restaurant_reservation#technical-requirements)
- [Tecnical Design](https://github.com/fokhrun/restaurant_reservation#tecnical-design)
    - [High Level Tech Stack](https://github.com/fokhrun/restaurant_reservation#high-level-tech-stack)
    - [High Level Architecture](https://github.com/fokhrun/restaurant_reservation#high-level-architecture)
- [Key Implementation Aspects](https://github.com/fokhrun/restaurant_reservation#key-implementation-aspects)
    - [Code Repository Structure](https://github.com/fokhrun/restaurant_reservation#code-repository-structure)
    - [Flask App Factory](https://github.com/fokhrun/restaurant_reservation#flask-app-factory)
        - [Flask Blueprints](https://github.com/fokhrun/restaurant_reservation#flask-blueprints)
    - [Data Model](https://github.com/fokhrun/restaurant_reservation#data-model)
    - [Flask Templates](https://github.com/fokhrun/restaurant_reservation#flask-templates)
    - [Handling Authentications](https://github.com/fokhrun/restaurant_reservation#handling-authentication)
    - [Handling Reservation](https://github.com/fokhrun/restaurant_reservation#handling-reservation)
        - [Authentication Related Flask Libraries](https://github.com/fokhrun/restaurant_reservation#authentication-related-flask-libraries)
        - [Password Security](https://github.com/fokhrun/restaurant_reservation#password-security)
        - [Authentication Blueprint](https://github.com/fokhrun/restaurant_reservation#authentication-blueprint)
        - [User Authentication](https://github.com/fokhrun/restaurant_reservation#user-authentication)
        - [Protecting Routes](https://github.com/fokhrun/restaurant_reservation#Protecting-Routes)
        - [Login Form](https://github.com/fokhrun/restaurant_reservation#login-form)
        - [Authentication Templates](https://github.com/fokhrun/restaurant_reservation#authentication-templates)
    - [Handling Reservation](https://github.com/fokhrun/restaurant_reservation#handling-reservation)
- [Future Improvements](https://github.com/fokhrun/restaurant_reservation#future-improvements)
- [Developer Guide](https://github.com/fokhrun/restaurant_reservation#developer-guide)
    - [Developer Environment](https://github.com/fokhrun/restaurant_reservation#developer-environment)
    - [VSCode Debugger](https://github.com/fokhrun/restaurant_reservation#vscode-debugger)
    - [Language/Library Requirements](https://github.com/fokhrun/restaurant_reservation#language/library-requirements)
    - [Working With Styling](https://github.com/fokhrun/restaurant_reservation#working-with-styling)
    - [Working With Custom Theme](https://github.com/fokhrun/restaurant_reservation#working-with-custom-theme)
    - [Testing](https://github.com/fokhrun/restaurant_reservation#testing)
    - [Running Tests](https://github.com/fokhrun/restaurant_reservation#running-tests)
    - [Test Cases](https://github.com/fokhrun/restaurant_reservation#test-cases)
- [Deployment to Heroku](https://github.com/fokhrun/restaurant_reservation#deployment-to-heroku)
    - [Preparation For Heroku Deployment](https://github.com/fokhrun/restaurant_reservation#preparation-for-heroku-deployment)
    - [Deployment Steps](https://github.com/fokhrun/restaurant_reservation#deployment-steps)
    - [Preparing Production Environment](https://github.com/fokhrun/restaurant_reservation#preparing-production-environment)
- [Credits](https://github.com/fokhrun/restaurant_reservation#credits)

## Overview [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

[Spice Magic](https://restaurant-binita-99be9591d7d4.herokuapp.com/) is a full stack restaurant website. The site provides 
- the site guests to see the restaurant menu
- the site owner to manage reservations for its restaurant guests through a centrally managed reservation database
- The site provides a role-based management of reservation database

## Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Functional Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

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
    3. `admin` can
        - create new type of tables 
        - remove any existing type of tables
        - create any new reservation slot
        - remove any existing reservation slot

### Technical Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
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

## Tecnical Design [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### High Level Tech Stack [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

- Front End: [Bootstrap Framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/) (HTML, CSS, Javascript)
- Back End: [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/) (Python)
    - ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Database: [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)
- Cloud: [Heroku](https://dashboard.heroku.com/apps)

### High Level Architecture [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

![High-level application architecture](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/flask_app_architecture.png)

## Key Implementation Aspects [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Code Repository Structure [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

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

### Flask App Factory [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Typically a flask app is created in a single-file version advocated by many sources. Such an application is created in the global scope, there is no way to apply configuration changes dynamically. So it is too late to make configuration changes, which can be important for unit tests. We deal with this problem we delay the creation of the application by moving it into a factory function that can be explicitly invoked from the script. This not only gives the script time to set the configuration, but also the ability  to create multiple application instances—another thing that can be very useful during testing.

Check `app\__init__.py` for more details.

#### Flask Blueprints [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Using [Blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints/) is an effective way to define routes in the global scope in factory app creation 
method. Using different blueprints for different subsystems of the application is a great way to keep the code neatly organized. The `main` blueprint covers 
the common routes in `app\main\views.py`. 

Check `app\__init__.py`, `app\main\__init__.py`, `app\main\views.py` and `app\main\erorrs.py` for more details.

### Data model [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

![Data Model](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/data_model.png)

### Flask Templates [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Flask leverages `jinja2` based [templates](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/) that basically injects input from backend to be rendered to the frontend.
It uses `render_template` function that is typically included in a function that handles a `route`. From `index.html` is a template in `app\main\templates` that will be rendered by `render_template` a function named `index()` that is decordated with `@app.route("\")` in `views.py`. When a request for such a route comes from the site, it leverages that `index()`
which at the end will call `render_template("main.index.html")`. Note that `main` is the blueprint where the route is managed. The function can provide additional parameters as 
keyword arguments, which can be input from the front end, but can also be additional parameters managed by the function. 

### Handling Authentication [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The site admin can reserve tables on behalf of any restaurant guests. However, the site provides fine-grained table reservation capability to authenticated users as follows:

- Site visitors can register using their name, email-addresses, passwords known to them. 
- Registered site `guests` can login using their email address and password to start using fine-grained reservation functionality
- `admin` is precreated by the site admin, who maintains the site. Once it is created, the `admin` can carry out advanced tasks on the reservations.

#### Authentication Related Flask Libraries [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We use the following Python packages
- `flask-login`: managing logged-in user sessions
- `werkzeug`: password hashing and verification
- `flask-wtf`: forms for login and registration

#### Password Security [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

`werkzeug`’s security module conveniently implements secure password hashing: 
- `generate_password_hash`: takes a plain-text password and returns the password hash as a string that can be stored in the user database. 
- `check_password_hash`: takes a password hash previously stored in the database and the password entered by the user, and returns `True` indicating 
that password is correct

These functions are used in the `User` model in `app/main/models.py`.

```
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
# ...
password_hash = db.Column(db.String(128))

@property
def password(self):
    raise AttributeError('password is not a readable attribute')

@password.setter
    def password(self, password):
    self.password_hash = generate_password_hash(password)

def verify_password(self, password):
    return check_password_hash(self.password_hash, password)
```

The password hashing function is implemented through a write-only property called `password`. When this property is set, the setter method will call
`generate_password_hash()` function and write the result to the `password_hash` field. Attempting to read the password property will return an error, 
as clearly the original password cannot be recovered once hashed.

The `verify_password()` method takes a password and passes it to `check_password_hash()` function for verification against the hashed version stored 
in the `User` model. If this method returns True, then the password is correct.

#### Authentication Blueprint [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The routes related to the user authentication subsystem will be added to a blueprint called `auth` that manages `login`, `logout`, and `register` routes. 

#### User Authentication [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

`flask-login` implements `is_authenticated`, `is_active`, `is_anonymous`, and `get_id` as properties and methods through `UserMixin` 
class. It needs to be implemented through `User` as follows:

```
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

flask-login needs to be initialized in the app factory function as follows. The `login_view` attribute of the `LoginManager` object sets the endpoint for the login page. Flask-Login will redirect to the login page when an anonymous user tries to access a protected page. Because the login route is inside a blueprint, it needs to be prefixed with the blueprint name.

```
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    ...
    login_manager.init_app(app)
    ...
```

`flask-login` requires the application to designate a function to be invoked when the extension needs to load a user from the database given its identifier. It is done through
`user_loader` decorator that register the function with `flask-login`, which will call it when it needs to retrieve information about the logged-in user. The user identifier will be passed as a string, so the function converts it to an integer before it passes it to the `SQLAlchemy` query that loads the user. The return value of the function must be the user object, or `None` if the user identifier is invalid or any other error occurred. Check out the following implementation:

```
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

For more details, check `app/main/models.py` ajd `app/__init__.py`.

#### Protecting Routes [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

To protect a route so that it can only be accessed by authenticated users, `FlaskLogin` provides a `login_required` decorator. An example of its usage follows:
```
from flask_login import login_required

@app.route('/a_protected_route')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
```

#### Login Form [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The login form that will be presented to users has a text field for the email address, a password field, a “remember me” checkbox, and a submit button. In addition
a set of validators needs to be implemented to ensure that wrong inputs are not passed. All of these are very straightforward to implement using `flask-wtf` and `wtforms`. 

Check out the following example, which is a skeleton for our implementation: 

```
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
```

#### Authentication Templates [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We implemented two templates namely `login.html` and `logout.html` that have similar designs. These templates can be found in the `app\templates\auth` folder. The rendered pages 
looks like the following screenshots.

![Register and Login](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/register_login_screens.png)

The main code that handles these templates are placed in `base.html` template using the following code snippet. 

```
<ul class="nav navbar-nav navbar-right">
{% if current_user.is_authenticated %}
<li><a href="{{ url_for('auth.logout') }}">Log Out</a></li>
{% else %}
<li><a href="{{ url_for('auth.login') }}">Log In</a></li>
{% endif %}
</ul>
```

The following image show how the rendering of these code snippets happen in the frontend. It also shows how flash message 
is shown to the user, when a user logs out or inputs wrong email address or password.

![Register and Login](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/login_logout_flash_screen.png)


### Handling Reservation [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

![Reservation wireframe](https://github.com/fokhrun/restaurant_reservation/blob/main/doc_images/wireframe-reservation.png)


## Future Improvements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Model [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
- must
    - User
        - validation for `email` to be actual email address
- should
    - User
        - make `role` non-nullable
- could
    - User

    -   

## Developer Guide [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Developer Environment [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

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
8. Initialize the database with right tables and their starter values by running `python .\iniatialize_db.py`. It creates 
    - 2 roles: `Admin` and `Guests`
    - 3 users: 1 `Admin` type and 2 `Guests` type
    - 6 tables of different capacitites
    - 6 (table) * 2 (slot per day) * 30 (days for November 2023) to create all reservation slots for November
9. Run the app `flask run --debug`
10. You can use `VSCode` as an editor

### VSCode Debugger [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
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

### Language/Library Requirements [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)


#### Non-compatible with flask-login and flask on versions [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

The current version of flask-login is not compatible with flask > 3.0. The fixes are in the way to make it work soon. More details can be found in this [issue](https://github.com/maxcountryman/flask-login/issues/805). Until then, it is recommended to use a widely accepted [temporary fix](https://github.com/maxcountryman/flask-login/issues/809).

### Working With Styling [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

This project leverages `bootstrap` for default themse and `node-sass` for custom themse for styling. Working with the both locally using `npm`, which requires `node.js`. 
Install `node.js` using this [link](https://nodejs.org/en/download). We recommend installing these packages in locally. It requires defining a `package.json` file 
where version of the libraties are mentioned. The packages are installed using the command `npm install <package>`, which installs it local node_modules directory, which
should be include in the `.gitignore` folder.  

#### Working with ready to use theme [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

To start leveraging ready made themse, we mainly work using `bootstrap`. In this project, we are working with `bootstrap@4.5`. To install `bootstrap`, run the following command: 

```
npm install bootstrap
```

To work with bootstrap, just have to copy-paste the following stylesheet <link> into the <head> of `base.html`, which is used in all other html files.

```
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
```

### Working With Custom Theme [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

We may want to influence coloring theme in a more custom manner than what `bootstrap` provides. A very good way to do it is using [`SCSS`](https://www.geeksforgeeks.org/what-is-the-difference-between-css-and-scss/), which is a superset of `CSS`. As `Flask` does not support `SCSS` natively, we need to use a tool like 
`node-sass` to compile `SCSS` files into `CSS`. To install `node-sass`, run the following command:

```
npm install node-sass  
```

To add global `SCSS` in a `Flask` application, we need to compile the SCSS files into CSS files. To do that, carry out the following steps:

- Create a directory name `static` in the `app` folder, if it doesn't exist already
- Inside the `static` directory, create a `scss` directory and a `css` directory
- Put the global SCSS file named `main.scss` in the `scss` directory. For example, the following main.scss file overrides the theme color of the site
    ```
    @import "theme_color";
    @import "./node_modules/bootstrap/scss/bootstrap";
    ```
    Here the `theme_color` is an another scss file where the theme colors are defined. 

- Compile the SCSS file into a CSS file using node-sass:

```
node-sass app/static/scss/main.scss app/static/css/main.css
```

- To use the `main.css` overriding bootstrap themes, link to the it using the url_for function. This line should be placed inside the <head> tag of `base.html`.

Here's an example of to do this in a Jinja2 template:

```
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/main.css') }}">
```

Note that every time there is a change in the SCSS files, we need to recompile them into CSS.

### Testing [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

#### Running Tests [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

- Add test codes in `tests` folder
- Run `flask test`

#### Test Cases [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

### Deployment To Production [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

#### Preparation For Heroku Deployment [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
- runtime.txt: `Python` run time version
    - `python-3.11.6`
- procfile: app exposed as `wsgi.py` with run command using `Gunicorn`
    - `web: gunicorn wsgi:app` 
- requirement.txt: Python dependencies
    - manually crafted or run `pip freeze > requirements.txt` in the local virtualenv
- "Eco Dynos Plan" in Heroku
- GitHub account connected to Heroku for free tier
- 

#### Deployment Steps [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)
- Create a new app in [Heroku](https://dashboard.heroku.com/apps)
- Fill the form with the app name, i.e., "restaurant-binita" and "Europe" as the region
- Click [addons](https://elements.heroku.com/addons)
    - Click [JawsDB MySQL](https://elements.heroku.com/addons/jawsdb), Choose Kitefin Shared (for free plan) and Install
        - You will get access to [Kitefin Server Dashboard](https://mysql.jawsdb.com/resource/dashboard) with information on 
            - `Host`
            - `Username`
            - `Password`
            - `Port`
            - `Database`
- Select `Settings`
    - Add `heroku/python` build pack
    - Add the following config vars that mimics `.env` file in the local environment
        - `JAWSDB_URL`: `Connection String` in Kitefin Server
        - `FLASK_CONFIG`: production
        - `DATABASE PROD`: `Database` in Kitefin Server
        - `DB_HOST_PROD`: `Host` in Kitefin Server
        - `DB_PASSWORD_PROD`: `Password` in Kitefin Server
        - `DB_PASSWORD_PROD`: `Password` in Kitefin Server
        - `SECRET_KEY`: <chosen secret> 
- Select `Deploy`
    - Choose "GitHub" as deployment method
    - Search the GitHub repo name `restaurant_reservation`. Once the repo is found, connect the repo.
    - Choose the default branch to deploy, i.e., the `main` branch
    - Click "Enable Automatic Deploys" which allows the app to be redeployed for every commit.
    - Click "Deploy Branch" for the first manual push.
- Select `Open app` to verify that the app got deployed.

#### Preparing Production Environment [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

1. `gunicorn` is not supported in In Windows. you can use `waitress` instead. Follow these [guide](https://stackoverflow.com/questions/11087682/does-gunicorn-run-on-windows)
2. To initialize the production database, change the `FLASK_CONFIG` to `production`
3. run `python .\iniatialize_db.py` to create the initial roles, users, tables, and reservations
4. Run the app by clicking the `Open App`
5. Verify by login to the site using the newly created credentials and checking the reservations visibile to different users
6. If there are errors, click `More` and use options, such as `View logs` or `Run console`

## Credits [^](https://github.com/fokhrun/restaurant_reservation#table-of-contents)

Photos by:
1. Chan Walrus: [front_image.jpg](https://www.pexels.com/photo/white-and-brown-cooked-dish-on-white-ceramic-bowls-958545/)
3. Mareefe: [about_1.jpg](https://www.pexels.com/photo/three-condiments-in-plastic-containers-674483/)
2. Gagan Kaur: [about_2.jpg](https://www.pexels.com/photo/a-woman-cooking-indian-food-3531700/)
