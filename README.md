# FPSO system api

Application desgined to serve a FPSO HTTP REST api

## Dependencies

* [FastAPI](https://fastapi.tiangolo.com/): fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints
* [Uvicorn](https://www.uvicorn.org/): ASGI web server implementation for Python.
* [Traefik](https://doc.traefik.io/traefik/): Traefik is an open-source Edge Router, used as a reverse-proxy
* [Docker](https://docs.docker.com/): Container Daemon

### Dev Dependencies (Optional)

* [Nix](https://nixos.org/download.html): Package Manager, creates reproducible enviroments
* [direnv](https://direnv.net/): env variables manager / loader

## Building

Using containers is prefered as it defines a standarized environment, so its much more likely that the following steps would work for everyone

### Build image

```bash
docker compose build
```

## Run

##
```bash
docker compose up
```

You also need to run database migrations:

```bash
docker compose run backend alembic upgrade head
```

Service will be running behind Traefik and can be acessible via localhost:8088

Check the OpenAPI documentation acessing `localhost:8088/redoc` or `localhost:8088/docs`

## Testing

You can run tests executing:

```bash
docker compose run backend pytest -vv --cov=app --cov-report=term-missing app
```


## Components

Application is developed using Python, as it is a friendly high-level general purpose language. HTTP Rest uses FastAPI, an high-perfomant ASGI compatible framework, that supports async requests and has great integration with OpenAPI and standarization, furthermore FastAPI, similar to Flask is lightweight and with fewer boilerplate code compared to other frameworks. Finally, the web server is run using Uvicorn, an implementation of [ASGI](https://asgi.readthedocs.io/en/latest/) supporting async request, websockets and much more.

Database of choice is the Relational (SQL) [PostgreSQL](https://www.postgresql.org/) chosen as it is open-souce and a industry standard with over 30 years of active development.

Traefik is the chosen reverse-proxy, acting as the gateway to the backend and dealing with routing, load balancing. Traefik was chosen as it has dynamic service discovery and good integration with Docker, specially docker-compose


## PART2 - Architecture

Assignment [PART 2](https://docs.google.com/drawings/d/1XFMLhY9DghglmFCSDRGmoQk8F6K_BayHDrNWyC-ROQg/edit?usp=sharing)
