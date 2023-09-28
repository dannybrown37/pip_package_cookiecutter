"""Module for pytest configuration"""


import json
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture(scope='session')
def test_json() -> SimpleNamespace:
    """Reads each JSON file in tests/data and puts in test_json namespace"""
    data = SimpleNamespace()
    for path in Path('tests/data').iterdir():
        if path.suffix == '.json':
            with path.open() as f:
                setattr(data, path.stem, json.load(f))
    return data
