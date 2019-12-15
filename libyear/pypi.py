import datetime

import requests


def get_pypi_data(name, version=None):
    """return a dictionary with pypi project data"""
    url = "https://pypi.org/pypi/%s/json" % name
    if version:
        url = "https://pypi.org/pypi/%s/%s/json" % (name, version)
    r = requests.get(url)
    if r.status_code < 400:
        return r.json()
    return {}


def get_version_release_dates(name, version):
    pypi_data = get_pypi_data(name)
    if not pypi_data:
        return None, None

    releases = pypi_data['releases']
    latest_version = pypi_data['info']['version']

    latest_version_date = releases[latest_version][-1]['upload_time_iso_8601']
    latest_version_date = datetime.datetime.strptime(latest_version_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    if version not in releases:
        version_data = get_pypi_data(pypi_data['info']['name'], version=version)
        version = version_data.get('info', {}).get('version')

    if version not in releases:
        return latest_version_date, latest_version_date

    version_date = releases[version][-1]['upload_time_iso_8601']
    version_date = datetime.datetime.strptime(version_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return version_date, latest_version_date


def get_lib_days(name, version, version_lt):
    cr, lr = get_version_release_dates(name, version)
    return (lr - cr) if cr else 0
