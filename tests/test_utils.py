from pathlib import Path

from libyear.utils import get_requirement_name_and_version, load_requirements


def test_loads_from_requirements_file_with_hashes():
    path = Path(__file__).parent / "data" / "requirements.txt"
    assert any(line.startswith("appdirs") for line in load_requirements(path))


def test_gets_name_and_version_from_requirements_file_with_hashes():
    path = Path(__file__).parent / "data" / "requirements.txt"
    results = {
        get_requirement_name_and_version(line) for line in load_requirements(path)
    }

    assert ("appdirs", "1.4.3", None) in results


def test_get_requirement_name_and_version():
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("xmltodict==0.10.0"))
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("xmltodict<=0.10.0"))
    assert(("xmltodict", "0.10.*", None) == get_requirement_name_and_version("xmltodict==0.10.*"))


def test_get_requirement_name_and_version_less_than():
    assert(("xmltodict", None, "0.10.0") == get_requirement_name_and_version("xmltodict<0.10.0"))


def test_get_requirement_name_and_version_no_version():
    no_version = (None, None, None)
    assert(no_version == get_requirement_name_and_version("xmltodict"))
    assert(no_version == get_requirement_name_and_version("xmltodict>=0.10.0"))
    assert(no_version == get_requirement_name_and_version("xmltodict>0.10.0"))
    assert(no_version == get_requirement_name_and_version("urllib3 @ https://github.com/urllib3/urllib3/archive/refs/tags/1.26.8.zip"))


def test_get_requirement_name_and_version_handle_spaces():
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("xmltodict == 0.10.0"))
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("xmltodict == 0.10.0   "))
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("    xmltodict == 0.10.0"))
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("xmltodict      == 0.10.0"))
    assert(("xmltodict", "0.10.0", None) == get_requirement_name_and_version("xmltodict ==       0.10.0"))


def test_get_requirement_name_and_version_handle_complex():
    assert(("requests[security]", "2.8.*", None) == get_requirement_name_and_version("requests[security] >= 2.8.1, == 2.8.*; python_version < \"2.7\""))
    assert(("requests[security]", "2.8.1", None) == get_requirement_name_and_version("requests[security] <= 2.8.1, == 2.8.*; python_version < \"2.7\""))
    assert(("requests[security]", None, "2.8.1") == get_requirement_name_and_version("requests[security] < 2.8.1, == 2.8.*; python_version < \"2.7\""))
    assert(("FooProject", "1.2", None) == get_requirement_name_and_version("FooProject == 1.2 --global-option=\"--no-user-cfg\""))
