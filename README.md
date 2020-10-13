# client for open weather api
I assume working on linux for this instructions

First create a virtual env

    $ python -m venv virtual_env_path

Then enter to the virtual env

    $ source /path/to/venv/bin/activate

To create the development environment run the following commands
from inside the virtual environment while on root of the project

    $ pip install -r requirements.txt
    $ pip install -r requirements-dev.txt

To run the tests run the following command

    $ pytest

This will run the tests to make sure the doce is behaving as 
intended. it won't send requests to the open weather api.

To ensure all the code is covered by tests one can run the following
command

    $pytest --cov=open_weather_api tests/

If one sees that some code is not covered by tests one can check 
which lines are note covered by the following command

    $ pytest --cov-report term-missing --cov=open_weather_api tests/

For deployment one can use the setup file to create the package with
the following command

    $ python setup.py sdist bdist_wheel

If wheel is not installed one must install it for the previous 
command to work with the following command

    $ pip install wheel

Once one have a package of the open_weather_api one can install it
via pip with the following command

    $ pip install /path/to/package

Or if loaded to remote repo configured with the local pip then just
run the command

    $ pip install open-weather-client