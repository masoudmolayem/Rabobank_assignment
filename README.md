# Rabobank_assignment

## Installation
To run the application on your machine, please follow the steps below:

1. Make sure you have the following dependencies installed:
   - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
   - [Docker](https://docs.docker.com/get-docker/)
   - [Docker Compose](https://docs.docker.com/compose/install/)

2. Clone the project repository to your local machine:
   ```
   git clone <repository-url>
   ```

3. Create a `.env` file in the project root directory. You can use the provided `.env.sample` file as a reference and update the environment variables as needed.

4. To run tests, execute the following command:
   ```
   docker compose -f docker-compose-deploy.yml run --rm kalaha_app sh -c "python manage.py test gamecore"
   ```
   
5. Start the application using Docker Compose by running the following command:
   ```
   docker compose -f docker-compose-deploy.yml up -d
   

# File Structure
```

├── assignment                     # The main directory of your Django project.
│   ├── assignment                 # The project's main settings and configuration directory.
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── todo                       # Contains the core logic and components of the todo app.
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── management             # Directory for custom management commands.   
│       │   ├── commands                    
│       │   │   ├── __init__.py
│       │   │   └── wait_for_db.py # wait for the database to be available.
│       │   └── __init__.py
│       ├── migrations
│       ├── models.py              # Defines the database models for the todo app.
│       ├── tests                  # Directory for tests related to the game logic.
│       │   ├── __init__.py
│       │   ├── test_models.py
│       │   ├── test_urls.py
│       │   └── test_views.py
│       ├── urls.py                # Definition file of the URL patterns
│       └── views.py               # Contains the view functions for handling HTTP requests
├── docker-compose-deploy.yml      # A Docker Compose configuration file for deploying application in a production environment.
├── docker-compose.yml             # A Docker Compose configuration file for local development and testing.
├── Dockerfile
├── proxy                          # Directory containing configurations for a proxy(nginix) server.
│   ├── default.conf.tpl
│   ├── Dockerfile
│   ├── run.sh
│   └── uwsgi_params
├── README.md
├── requirements.txt
└── scripts                        # Directory for scripts related to the project.
    └── run.sh
 

```

