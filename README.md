# Todoist CLI

This is a CLI for interacting with Todoist.

## Project status: Alpha

This project has just started and is not ready for anyone to use.

## Installation

1. Clone this Repo
2. Create and activate a venv
`python3 -m venv venv`
`source venv/bin/activate`
3. Install requirement
`pip install -r requirements.txt`
4. Copy sample.config.py to config.py
`cp sample.config.py config.py`
5. Replace API Token in config.py (found in Todoist Settings under Integrations)

## Usage

### Create a task

`python create-task.py task_name`
