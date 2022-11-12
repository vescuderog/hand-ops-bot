# HandOps bot

![Python application](https://github.com/vescuderog/hand-ops-bot/workflows/Python%20application/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

HandOps bot is a Python library for easy operation with [Slack](https://slack.com/intl/es-la/) and [GitLab](https://gitlab.com/).

It also exposes all opportunities of [Slack's Real Time Messaging API](https://api.slack.com/rtm).

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

### Environment variables

* `APP_ENV` - the deployment environment: development, testing, staging or production
* `RTM_MODE` - set to `True` to open websocket connection to listen to incoming messages (default, `False`)
* `BOT_NAME` - the bot name
* `SLACK_API_TOKEN` - the bot user OAuth access token
* `SLACK_CHANNEL` - the slack channel

## Usage

To run HandOps bot on your local machine, you can set the environment variables using a [.env file](https://github.com/theskumar/python-dotenv). To do this, create an .env file in the main project directory with the following variables:

```bash
APP_ENV="development"
RTM_MODE=False
BOT_NAME="hand_ops"
SLACK_API_TOKEN="YOURSLACKAPITOKEN"
SLACK_CHANNEL="YOURSLACKCHANNEL"
```

Then, run the development server:

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
