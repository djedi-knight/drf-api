# Django Rest Framework (DRF) API

A collection of example REST API projects using [DRF](http://www.django-rest-framework.org/)

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install the following before installing the application:

- [Python3](https://www.python.org/downloads/)
- [virtualenv](https://pypi.python.org/pypi/virtualenv)

### Installation

The following will get a development environment for this application
up and running.

1. Setup a Virtual Environment

```
virtualenv -p /usr/local/bin/python3 venv
```

*Note: the path to Python3 may differ depending on your setup*

2. Activate the Virtual Environment

```
source venv/bin/activate
```

*Note: to deactivate the environment, run the following command:*

```
deactivate
```

3. Install the Required Packages

```
pip install -r requirements.txt
```

4. Run the server

```
fab runserver
```

## Development

### Creating a Project

Run the following command to create a new project:

```
django-admin startproject project_name
```

Where *project_name* is the name of the project to create

### Creating an Application

Run the following command to create a new application:

```
python3 manage.py startapp app_name
```

Where *app_name* is the name of the app to create

### Creating a User

Run the following command to create a new superuser:

```
python3 manage.py createsuperuser
```

### Creating Migrations

Run the following command to create a new migration:

```
python3 manage.py makemigrations
```

### Applying Migrations

Run the following to apply the latest migrations to the database:

```
python3 manage.py migrate
```

## Packages

The following packages are currently being used:

- [django](https://pypi.python.org/pypi/django)
- [djangorestframework](https://pypi.python.org/pypi/djangorestframework)
- [coreapi(https://pypi.python.org/pypi/coreapi)
- [fabric3](https://pypi.python.org/pypi/fabric3)

## Authors

* **Shawn Daichendt** - [djedi-knight](https://github.com/djedi-knight)

## Acknowledgments

* [DRF REST API Tutorial (auth_api)](https://medium.com/@ktruong008/building-an-api-with-django-rest-framework-and-class-based-views-75b369b30396)
* [DRF REST API Tutorial (bookreview)](https://code.tutsplus.com/tutorials/beginners-guide-to-the-django-rest-framework--cms-19786)
* [DRF REST API Tutorial (bucketlist)](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1)
