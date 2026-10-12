# PingWatch

A command-line tool that checks whether your websites and services are up,
how fast they respond, and why they fail when they don't.

![pingwatch logo](docs/logo.jpg)

## Features

- Checks multiple targets from a single JSON config file
- Reports status, HTTP code, response time and the reason for any failure
- Watch mode (coming in v2, trust)

## Install

With uv:

```
uv tool install https://github.com/Jinmi-codes/pingWatch/releases/download/v1.0/pingwatch-0.1.0-py3-none-any.whl
```

Or download the `.whl` from the [Releases page](https://github.com/Jinmi-codes/pingWatch/releases/download/v1.0/pingwatch-0.1.0-py3-none-any.whl) and run:

```
pip install pingwatch-0.1.0-py3-none-any.whl
```

Requires Python 3.13 or newer.

## Usage

```
pingwatch config.json
```

## Configuration

Copy `config.example.json` to `config.json` and edit it:

```json
{
    "defaults": [],
    "targets": [
        {
            "name":"Google",
            "url":"https://google.com"
        },
        {
            "name":"Netlfix",
            "url":"https://netlix.com"
        }
    ]
}
```

Name and Url are required!! It won't be accepted as a target otherwise.
Defaults can simply be ignored until later versions.

## Example output

```
Name: Google, Status: UP  HTTP-Code:200, Time:01.728926
Name: Netlfix, Status: UP  HTTP-Code:200, Time:01.958453
```

## How it works
PingWatch uses the request package to probe websites. 
You provide a JSON file of websites you want, and PingWatch scans through and returns Status, HTTP Code and time taken to receive a response from the server. 
It's a project I built for Prep week 2 of Terra, A Hack Club YSWS. 

