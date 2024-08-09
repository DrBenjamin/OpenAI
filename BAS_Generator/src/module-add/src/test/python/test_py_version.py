# This is a sample file that can contain any unit tests for your python code. 
# You can use your own testing frameworks as part of the tests too.
import pytest
from py_version import py_version_fn
from unittest.mock import MagicMock
from snowflake.snowpark import Session
from snowflake.snowpark.functions import lit
from functools import partial

@pytest.fixture()
def session():
    session = Session.builder.config('local_testing', True).create()
    yield session
    session.close()

# Unit tests for UDF
def test_py_version_fn():
    assert py_version_fn() == '3.10'

