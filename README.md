# scuole
*(It's Italian for "schools.")*

Public Schools 3!

## Setup

This project assumes you are using the provided docker postgreSQL database build. Make sure docker is up and running, then run:

```sh
make docker/db
```

This will create the data volume and instance of PostgreSQL for Django. To ensure Django knows where to look, you need to set the `DATABASE_URL`. If you are not using the docker provided database, use `DATABASE_URL` to tell the app what you've done instead.

```sh
export DATABASE_URL=postgres://docker:docker@docker.local:5432/docker
```

From there, the app should be runnable as normal.

Fire up pipenv:

```sh
pipenv --three
```

Install dependencies via pipenv:

```sh
pipenv install --dev
```

Run pipenv:

```sh
pipenv shell
```

Check for any migrations:

```sh
python manage.py migrate
```

Alternatively, you can load in last year's data. This command will drop your database, create a new one and run migrations before loading in the data:

```sh
make local/reset-db-bootstrap-latest
```

Check out the makefile for more commands.

Then see if it'll run:

```sh
python manage.py runserver
```

All good? Let's go!

## Admin

This likely won't have an admin interface, but you are welcome to use it to check out how things are getting loaded. First, you'll need to create a super user. (If you ever blow away your database, you'll have to do it again!)

```sh
python manage.py createsuperuser
```

Then, after a `python manage.py runserver`, you can visit [http://localhost:8000/admin](http://localhost:8000/admin) and use the credentials you setup to get access. Every thing will be set to read-only, so there's no risk of borking anything.


## Analysis

The analysis directory is used for incorporating schools with other datasets. These include:

1) A-F scores

We merge the slugs in the schools database with A-F scores for each campus; this is done to link back to their pages in our schools app in our [grade lookup tool](https://www.texastribune.org/2019/08/15/texas-schools-grades-accountability/). Data with A-F scores from TEA gets put into the `raw_data` manually. The spreadsheet with slugs for campus can be generated and put into that directory by running:

```sh
python manage.py exportslugs
```

After those files are in put in that directory, run everything inside of `analysis.ipynb` to spit out a spreadsheet in the `output` directory, which will then be loaded into a Google spreadsheet to be used with the lookup tool.

