from pathlib import Path

from libyear.utils import get_requirement_name_and_version, load_requirements, load_pipfile


def test_loads_from_requirements_file_with_hashes():
    path = Path(__file__).parent / "data" / "requirements.txt"
    assert any(line.startswith("appdirs") for line in load_requirements(path))


def test_gets_name_and_version_from_requirements_file_with_hashes():
    path = Path(__file__).parent / "data" / "requirements.txt"
    results = {
        get_requirement_name_and_version(line) for line in load_requirements(path)
    }

    assert ("appdirs", "1.4.3", None) in results


def test_loads_from_pipfile():
    path = Path(__file__).parent / "data" / "Pipfile"
    assert set(load_pipfile(path)) == set(
        ['idna==2.7', 'prettytable>=0.7.2', 'toml', 'requests>=2.0.0', 'docker<=4.4.4', 'random_lib2==2.0.0'])
