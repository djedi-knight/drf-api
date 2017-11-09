# Django Rest Framework (DRF) API

An example REST API application using [DRF](http://www.django-rest-framework.org/)

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install the following before installing the application:

1. [Install Python3](https://www.python.org/downloads/)

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

3. Run the server

```
python3 manage.py runserver
```

## Development

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

* [DRF REST API Tutorial](https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1)
