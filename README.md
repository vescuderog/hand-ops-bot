# HandOps bot

[![wercker status](https://app.wercker.com/status/a5ca5229d8cb0a5d4995ec9cf8e60d6e/s/ "wercker status")](https://app.wercker.com/project/byKey/a5ca5229d8cb0a5d4995ec9cf8e60d6e)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

HandOps bot is a Python framework with the goal of being a bridge between the collaboration tool [Slack](https://slack.com/intl/es-la/) and the DevOps tool [GitLab](https://gitlab.com/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For building and running the application you need:

- [Python 3](https://www.python.org/) 
- [Pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

### Installing

Create a virtual environment and activate it (Windows):

```shell
py -m venv env
.\env\Scripts\activate
```

Now that you’re in your virtual environment you can install the project packages:

```bash
pip install -r requirements.txt
```

If you want to leave your virtual environment:

```bash
deactivate
```

## Usage

If you want to run HandOps bot on your local machine, you can set the environment variables using a [.env file](https://github.com/theskumar/python-dotenv). To do this, create an .env file in the main project directory with the following variables:

```bash
APP_ENV="development"
API_MODE=True
SECRET="YOURSECRET"
SLACK_API_TOKEN="YOURSLACKAPITOKEN"
SLACK_CHANNEL="YOURSLACKCHANNEL"
```

Run the development server:

```bash
python handops.py
```

## Built With

* [Flask](https://palletsprojects.com/p/flask/)
* [Python slackclient](https://github.com/slackapi/python-slackclient)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
