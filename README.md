# web-assignment

## Enabling virtual environment

```On Windows
.venv/Scripts/activate.bat
```

```On Unix or MacOS
source .venv/bin/activate
```

## Running the server

```On Windows
./run.bat
```

```On Unix or MacOS
./run.sh

## Running unit tests and generating a coverage report

```
coverage run test.py
coverage report main.py
```

```For an html report
coverage html
```

## Running robot framework tests
```
robot test.robot
```

## Exiting virtual environment
```
deactivate
```
