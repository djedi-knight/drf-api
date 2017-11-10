# Django Rest Framework (DRF) API

An example REST API application using [DRF](http://www.django-rest-framework.org/)

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

3. Install the Required Packages

```
pip install -r requirements.txt
```

4. Run the server

```
python3 manage.py runserver
```

## Development

### Creating a User

Run the following command to create a new super-user:

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

## Authors

* **Shawn Daichendt** - [djedi-knight](https://github.com/djedi-knight)

## Acknowledgments

* [DRF REST API Tutorial (bucketlist)](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1)
* [DRF REST API Tutorial (auth_api)](https://medium.com/@ktruong008/building-an-api-with-django-rest-framework-and-class-based-views-75b369b30396)
