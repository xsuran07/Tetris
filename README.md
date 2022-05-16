# Tetris

This project provides an implementation of the classical old-school game Tetris. Apart from the game itself, the application also includes a brief tutorial. It demonstrates all the game mechanisms.

## Build

The recommended Python version is **3.8**. For the management of the dependencies, [pipenv](https://pipenv.pypa.io/) is used. So make sure you have it installed:

```
$ pip install pipenv
```

After that, all necessary Python packages can be installed with:

```
<project-root> $ pipenv install --deploy
```

## Usage

The main script is situated in `bin/` directory and can be run like any other Python script. To ensure that it has access to all packages installed during the build phase, use the following command:

```
<project-root> $ pipenv run python ./bin/tetris.py
```
