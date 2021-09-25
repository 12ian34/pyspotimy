# pyspotimy

A selection of tools for personal spotify streaming analysis. Currently in alpha. You can do two things:

1. Get user's top played tracks via `spotipy`.
1. Parse and analyse streaming data history via the official [Spotify personal data download](https://www.spotify.com/us/account/privacy/).

# installation

1. if you don't have one already, create an API app
    1. log into the Spotify Developers dashboard
    1. follow the instructions to create an app
    1. set the callback_uri to `http://127.0.0.1:5050/callback/q`

1. clone git repo, e.g. via `github-cli`
    ```
    gh repo clone 12ian34/pyspotimy
    ```
1. create python virtual environment, and activate it e.g. via `python-virtualenv`
    ```
    cd pyspotimy
    python -m venv .venv
    source .venv/bin/activate
    ```
1. install dependencies
    ```
    pip install -e .
    ```
1. set environment variables:
    ```
    export SPOTIFY_ID="<your API app client id>"
    export SPOTIFY_SECRET="<your API app client secret>"
    export SPOTIFY_CB_URI="http://127.0.0.1:5050/callback/q"
    ```

# usage [WIP]

1. `python main.py`

# limitations [WIP]

- 

# todo [WIP]

- 
