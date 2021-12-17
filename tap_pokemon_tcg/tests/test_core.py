"""Tests standard tap features using the built-in SDK tests library."""

import os

from singer_sdk.testing import get_standard_tap_tests

from tap_pokemon_tcg.tap import TapPokemonTCG

SAMPLE_CONFIG = {
    "api_key": os.environ("TAP_POKEMON_TCG_API_KEY")
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapPokemonTCG,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()
