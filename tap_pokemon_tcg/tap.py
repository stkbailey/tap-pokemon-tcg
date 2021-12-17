"""PokemonTCG tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_pokemon_tcg.streams import (
    CardsStream,
    SetsStream,
)

STREAM_TYPES = [
    CardsStream,
    SetsStream,
]


class TapPokemonTCG(Tap):
    """PokemonTCG tap class."""
    name = "tap-pokemon-tcg"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The API Key to authenticate against the API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
