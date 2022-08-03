# TradeCompeteAndCollect
### Set Up A Virtual Environment:

First thing need to do, is set up our virtual environment, a virtual environment helps us run several versions of python/django right on the same machine (e.g we could have two different python/django projects running on different versions, to avoid them clashing and to give us room to run them both without errors, the virtual environment comes to our rescue. One virtual environment = one python/django version).

### To set up our virtual environment:

- pip/pip3 install virtualenv

After installation, we should create a virtual environment that would enable us use a preferred django version of our choice:
- virtualenv env_name (env_name should be replaced with the preferred name of the environment)

### Activating Virtual Environment:
Now as we have setup our virtual env, we need to enable it, to enable the virtual env that we've just created (`env_name`):

To activate the virtual environment for linux/Mac OS:

- source env_name/bin/activate

For windows:

- env_name/script
- activate


### Install the required packages using:
Now it's time to create the required packages (including django):

- pip install -r requirements.txt

### Making Migrations:

Migrations helps us make changes to our database schema without losing any data, each time we create a new model or make changes to a current one and run migrations, it helps update our database tables with the schemas without having to go through all the stress of dragging and recreating the database ourselves.

To run our migrations:

- python manage.py migrate


### Run the project

- python manage.py runserver
