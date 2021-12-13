import pytest
import sys


@pytest.mark.skip(reason="Unable to test")
def test_example():
    assert True


@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8 or later")
def test_skip_os_ver():
    print(sys.version_info)
    assert True
