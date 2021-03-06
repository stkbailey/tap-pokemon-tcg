"""Stream type classes for tap-pokemon-tcg."""

from pathlib import Path

from tap_pokemon_tcg.client import PokemonStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class CardsStream(PokemonStream):
    """Define custom stream."""

    name = "cards"
    path = "/cards"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "cards.json"


class SetsStream(PokemonStream):
    """Define custom stream."""

    name = "sets"
    path = "/sets"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "sets.json"
