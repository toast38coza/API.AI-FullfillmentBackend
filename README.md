# API.AI-FullfillmentBackend

## Setup:

```
pip install -r requirements.txt -r requirements-dev.txt
python manage.py runserver
```

or with docker:

```
docker-compose up -d
```

## Deploy

Create a digital ocean droplet using the Docker droplet

Edit `inventory` file to have the correct IP address of your target server

Then just run:

```
ansible-playbook deploy.yml -i inventory
```

You can run that at any time to run a deploy