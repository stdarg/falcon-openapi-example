# falcon-openapi-example
An example project using falcon-openapi

To run, do the following:

```bash
$ pipenv sync --dev
$ pipenv run gunicorn example.app
```

To make a request:

```bash
$ curl -vvv http://localhost:8000/example/v1/health
```
