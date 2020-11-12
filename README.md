# web-assignment

## Enabling virtual environment
On Windows
```shell
.\.venv\Scripts\activate.bat
```

On Unix or MacOS
```shell
source .venv/bin/activate
```

## Running the server
On Windows
```shell
.\run.bat
```

On Unix or MacOS
```shell
./run.sh
```

## Running unit tests and generating a coverage report
Run the test script
```shell
coverage run test.py
```

For a report in the command line output
```shell
coverage report main.py
```

For an html report
```shell
coverage html
```

## Running robot framework tests
```shell
cd && robot test.robot && cd ..
```

## Exiting virtual environment
```shell
deactivate
```
