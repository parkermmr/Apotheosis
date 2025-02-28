## How to get started

### Install

First install the depencies from the lock using poetry install.
```
poetry install
```

Then following the install build and run the dockerfile with the below:
```
docker build -t my-mkdocs-site .
docker run -d -p 8000:80 my-mkdocs-site
```

If you want to host the docs from a terminal locally use:
```
poetry mkdocs build
poetry run mkdocs serve
```
