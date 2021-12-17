# tap-pokemon-tcg

`tap-pokemon-tcg` is a Singer tap for the official [Pokemon Trading Card Game website](https://tcg.pokemon.com/). It is based on the [v2 API](https://pokemontcg.io/) provided to developers.

The tap contains two streams -- `cards` and `sets` -- that are set to full table replication. The tap is built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

You can install the tap vai the Github repo:

```bash
pip install git+https://github.com/stkbailey/tap-pokemon-tcg
```

## Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`

## Settings

| Setting| Required | Default | Description |
|:-------|:--------:|:-------:|:------------|
| api_key| True     | None    | The API Key to authenticate against the API service |

A full list of supported settings and capabilities is available by running: `tap-pokemon-tcg --about`

## Usage

You can easily run `tap-pokemon-tcg` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-pokemon-tcg --version
tap-pokemon-tcg --help
tap-pokemon-tcg --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_pokemon_tcg/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-pokemon-tcg` CLI interface directly using `poetry run`:

```bash
poetry run tap-pokemon-tcg --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-pokemon-tcg
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-pokemon-tcg --version
# OR run a test `elt` pipeline:
meltano elt tap-pokemon-tcg target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
