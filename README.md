# Todoist CLI

This is a CLI for interacting with Todoist.

## Project status: Alpha

This project has just started and is not ready for anyone to use.

## Installation

1. Clone this Repo
2. Install requirement
`uv sync`
3. Create .env file with your Todoist api key
`cp .env.sample .env`
4. Replace API Token in .env (found in Todoist Settings under Integrations)

## Usage

`make run`

### Create a task

`uv run python create-task.py task_name`
