# autoconnect-24online

A simple cross-platform python script to automate logging into 24online captive portal installed on university wifi's.

## Background

I'm fed up of logging into the captive portal as my university's IT department randomly decides to force a logout to all the connected devices (multiple times a day!).

## Installation

1. Simply clone this repository.

```sh
$ git clone https://github.com/SyedAhkam/autoconnect-24online
$ cd autoconnect-24online
```

2. Copy pre-configuration from `.env.example`

```sh
$ cp .env.example .env
```

> It has `SERVER_NAME` and `PROFILE_NAME` already set up for bennett university.

3. Set your `USERNAME` and `PASSWORD` in `.env` using your favourite text editor.

4. Install python dependencies.

```sh
$ pip install -r requirements.txt
```

## Usage

```sh
$ python main.py
```

## Automatic periodic execution

There are a couple of ways to do that.

1. Cron Jobs (recommended)
2. Systemd timers
3. Desktop Autostart (would require adding a loop in script, not the best way)
