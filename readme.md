## Challenge

A pet store decides they want a way to keep track of their dogs and cats.
They said they want to be able to store these attributes:

* name
* breed
* birthday

In addition, names are no longer than 30 characters and breed is no longer than 50 characters.

The petstore wants to be able to:

* list all pets
* list all dogs
* list all cats
* view one dog
* view one cat
* add a dog
* add a cat
* delete a dog
* delete a cat

As being part of the team that makes this system, you must create a Django project that has endpoints that can provide these functionalities.  Ideally, Django Rest Framework should be used.

## Solution

### Environment

This application is designed to run in a Python 3.4
[virtualenv](https://virtualenv.pypa.io/en/latest/).

### Requirements

Use `pip install` to install these required packages.

* Django
* Markdown
* djangorestframework
* selenium

### Running

Run the test server with `python manage.py runserver`. View the application in
a web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Testing

Run the tests with `python manage.py test`. See
[Testing in Django](https://docs.djangoproject.com/en/1.8/topics/testing/) for
more information.
