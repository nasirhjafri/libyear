import argparse
import os
import sys
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader
from pathlib import Path
from unittest import mock

import pytest


def load_libyear_module():
    """ As the module has no extension, this workaround is needed to load """
    libyear_path = str(Path(__file__).parent.parent / "libyear/libyear")
    spec = spec_from_loader("libyear", SourceFileLoader("libyear", libyear_path))
    libyear = module_from_spec(spec)
    spec.loader.exec_module(libyear)
    sys.modules['libyear'] = libyear
    return libyear


libyear = load_libyear_module()


@pytest.fixture(scope='module')
def vcr_config():
    return {
        'decode_compressed_response': True
    }


@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    # Put all cassettes in tests/cassettes/{module}/{test}.yaml
    return os.path.join('tests/cassettes/', request.module.__name__)


@pytest.mark.vcr()
def test_libyear_main_output(capsys):
    requirements_path = str(Path(__file__).parent / 'data' / 'requirements.txt')

    with mock.patch(
        'libyear.argparse.ArgumentParser.parse_args',
        return_value=argparse.Namespace(r=requirements_path, sort=False)
    ):
        libyear.main()

    out, err = capsys.readouterr()
    out_lst = out.split("\n")

    assert err == ''
    assert out_lst[0:3] == '''\
+-------------------+-----------------+----------------+-----------------+
|      Library      | Current Version | Latest Version | Libyears behind |
+-------------------+-----------------+----------------+-----------------+'''.split("\n")

    ref_lst = '''\
|     pyparsing     |      2.4.5      |     2.4.7      |       0.4       |
|      pathspec     |      0.6.0      |     0.8.1      |       1.1       |
|     packaging     |       19.2      |      20.8      |       1.23      |
|     typed-ast     |      1.4.0      |     1.4.1      |       0.61      |
|     virtualenv    |      16.6.2     |     20.2.2     |       1.4       |
|     pre-commit    |      1.20.0     |     2.9.3      |       1.11      |
|       regex       |    2019.12.9    |   2020.11.13   |       0.93      |
|       pyyaml      |      5.1.1      |     5.3.1      |       0.78      |
|        mypy       |      0.750      |     0.790      |       0.86      |
|       attrs       |      19.1.0     |     20.3.0     |       1.68      |
|      watchdog     |      0.9.0      |     1.0.2      |       2.31      |
|      identify     |      1.4.5      |     1.5.10     |       1.44      |
|      colorama     |      0.4.1      |     0.4.4      |       1.89      |
|       black       |     19.10b0     |     20.8b1     |       0.83      |
|         py        |      1.8.0      |     1.10.0     |       1.81      |
|   more-itertools  |      7.0.0      |     8.6.0      |       1.59      |
|   pytest-testmon  |      0.9.16     |     1.0.3      |       1.39      |
|       isort       |      4.3.17     |     5.6.4      |       1.52      |
|        toml       |      0.10.0     |     0.10.2     |       2.08      |
|      nodeenv      |      1.3.3      |     1.5.0      |       1.8       |
|       pytest      |      4.4.0      |     6.2.1      |       1.71      |
|        tox        |      3.14.2     |     3.20.1     |       0.85      |
|      pyflakes     |      2.1.1      |     2.2.0      |       1.11      |
|    atomicwrites   |      1.3.0      |     1.4.0      |       1.24      |
|       flake8      |      3.7.7      |     3.8.4      |       1.6       |
|      coverage     |      4.5.3      |     5.3.1      |       1.78      |
|        six        |      1.12.0     |     1.15.0     |       1.45      |
|   flake8-bugbear  |      19.3.0     |    20.11.1     |       1.66      |
|       click       |       7.0       |     7.1.2      |       1.59      |
|  mypy-extensions  |      0.4.1      |     0.4.3      |       1.15      |
|      appdirs      |      1.4.3      |     1.4.4      |       3.18      |
| typing-extensions |     3.7.4.1     |    3.7.4.3     |       0.82      |
|        cfgv       |      2.0.1      |     3.2.0      |       1.03      |
|    pycodestyle    |      2.5.0      |     2.6.0      |       1.28      |\
'''.split('\n')

    def table_sort(s):
        """remove `|` + any spaces, in order to get alphabetic sort of first column"""
        return s.lstrip(" |")

    assert sorted(out_lst[3:-3], key=table_sort) == sorted(ref_lst, key=table_sort)

    assert out_lst[-3:] == '''\
+-------------------+-----------------+----------------+-----------------+
Your system is 47.2 libyears behind
'''.split('\n')
