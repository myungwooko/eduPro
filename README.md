# eduPro server


## Tech

Using Library

* [Django] - Python Web Application Framework
* [Django Rest Framework] - RESTFul Web API

## Installation

to run the program greater, equal than [python] 3.5 version

### Step.1 Install dependent packages

```sh
$ pip3 install virtualenv
$ virtualenv -p python venv
$ source venv/bin/activate
$ pip install -r requirements.txt

* if your installment stuck at "error: command 'gcc' failed with exit status 1"
Use below command
LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient


```

Starting server through basic setting file like below.
```sh
$ python manage.py migrate
$ python manage.py runserver
```

Starting server through specific setting file like below.
It referencs running environment value of 'RUNNING_ENV'. Vlaues of 'RUNNING_ENV' are `base`, `local`, `development`, `stage`, `production` 
- base : basic setting
- local : setting for local development
- development : setting for development deploy 
- stage : setting for stage deploy 
- production : setting for production deploy 


> Each setting file's definitions are in `settings` directory, Sensitive information like password has to be defined in `secrets.json` under `settings` directory,

```sh
$ export RUNNING_ENV=development
$ python manage.py runserver
```


After starting the server, put the address of the server for checking it works.
```sh
http://127.0.0.1:8000
```

## Docker

Docker You can install and deploy by using Docker container.

Basically, docker that is applied to this project uses port 80
When it is ready to build, it builds image, using Dockerfile.

```sh
$ docker build -t server .
```

When build process was finished properly, create a container that is based the Docker image.
When you create the container, map the port to connect and host port. 
The example below maps host port 8000 and container port 80(that is exposed at Dockerfile).   

```sh
$ docker run -d -p 8000:80 server
```

When container was created properly, type the server address in your browser

```sh
127.0.0.1:8000
```

## API Document
Document fot API is automatically created through Swagger.

Swagger API documentation's address is `/api/swagger`.
> Ex) /api/swagger


### Branch Naming & Merge Request Rule
when process is going, branch naming rule is like below.
- master : Storage for code of relased version  
- develop : Storage for code on developing process
- feature-`{issue_number}` : Case incluing new feature. (ex: adding APP, Endpoint and etc)
- improve-`{issue_number}` : Case of that there is improvements for code of previous version. (ex: refactoring, improvement and etc)
- fix-`{issue_number}` : Case of bug fix. 
 
Sequence of  merge request is (`feature-*`, `improve-*`, `fix-*`) -> `develop` -> `master` 


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [fount logo]: <https://fount.co/wp-content/uploads/2017/07/fount-ci@2x.png>
   [python]: <https://www.python.org/>
   [Django]: <https://www.djangoproject.com/>
   [Django Rest Framework]: <http://www.django-rest-framework.org/>
   [drf-yasg]: <https://drf-yasg.readthedocs.io/en/stable/>
   [Celery]: <http://www.celeryproject.org/>
   