## Getting started

just use ```docker-compose up``` command and you ready to go

for easily creating admin user you can you helper script
```./docker-manage.sh createsuperuser```

## Load questionnaires

Use ```loadquestionnaires``` manage command for loading questionnaires structure from JSON file

Example:

```python manage.py loadquestionnaires questionnaires.json```

For docker users, load ```questionnaires.json``` file to container first by using
```docker cp``` [command](https://docs.docker.com/engine/reference/commandline/cp/)

For example, given ```9c5c3f055843``` is the container ID copying
questionnaires file to a container is as simple as
```docker cp ./questionnaires.json 9c5c3f055843:/app/questionnaires.json```

To obtain container ID use ```docker ps``` command, and look for ```ariana_local_django```

Than you can execute python manage.py command inside docker container

```docker-compose exec django python manage.py loadquestionnaires questionnaires.json```
