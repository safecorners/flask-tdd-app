# Python Development Workflow

```bash
python -m pip install virtualenv
python -m venv .venv
source .venv ./venv/bin/activate
```

```bash
python -m pip install poetry
poetry init
```

## Configuration

> Use an environment variable to switch between the configurations. This can be done from outside the Python interpreter and makes development and deployment much easier because you can quickly and easily switch between different configs without having to touch the code at all. If you are working often on different projects you can even create your own script for sourcing that activates a virtualenv and exports the development configuration for you.

## Reference

- [](https://serpapi.com/blog/python-virtual-environments-using-virtualenv-and-poetry/)
