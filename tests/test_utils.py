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
