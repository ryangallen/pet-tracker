# Pet Tracker

A demo app built with Django and AngularJS, and Django Rest Framework for the API.

## Scenario/Requirements

A pet store decides they want a way to keep track of their dogs and cats.
They said they want to be able to store these attributes:

* name
* breed
* birthday

The pet store wants to be able to:

* list all pets
* list all dogs
* list all cats
* view one dog
* view one cat
* add a dog
* add a cat
* delete a dog
* delete a cat

## Screenshots

### Login
![Login](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/00-login.png)
### Dashboard
![Dashboard](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/01-dashboard.png)
### Dashboard filtered
![Dashboard filtered](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/02-dashboard-filtered.png)
### Add a pet
![Add a pet](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/04-add-a-pet.png)
### Select animal type
![Select animal type](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/05-select-animal-type.png)
### Select animal breed
![Select animal breed](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/06-select-animal-breed.png)
### Animal details form
![Animal details form](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/07-animal-details-form.png)
### Animal added
![Animal added](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/08-animal-added.png)
### Animal details
![Animal details](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/09-animal-details.png)
### Delete animal
![Delete animal](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/10-delete-animal.png)
### Confirm delete animal (blank)
![Confirm delete animal (blank)](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/11-confirm-delete-animal-blank.png)
### Confirm delete animal (name entered)
![Confirm delete animal (name entered)](https://github.com/ryangallen/pet-tracker/blob/eef3c39ad7c32a35e8f878d1267389789f4b212f/12-confirm-delete-animal-name-enetered.png)

## Dev Environment

This application is designed to run in a Python 3.4
[virtualenv](https://virtualenv.pypa.io/en/latest/).

## Requirements

Use `pip install` to install these required packages.

* Django
* Markdown
* djangorestframework
* selenium

## Running

Run the test server with `python manage.py runserver`. View the application in
a web browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Testing

Run the tests with `python manage.py test`. See
[Testing in Django](https://docs.djangoproject.com/en/1.8/topics/testing/) for
more information.

Funcational tests are built with
[Selenium](https://selenium-python.readthedocs.org/) and run in
[Mozilla Firefox](https://www.mozilla.org/en-US/firefox/products/). See the
Selenium [Webdriver API](https://selenium-python.readthedocs.org/api.html) docs
for testing in other browsers.

## License

The MIT License (MIT)

Copyright (c) 2017 Ryan Allen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
