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


def get_version(pypi_data, version, lt=False):
    if not version:
        return None

    releases = pypi_data['releases']
    if version not in releases:
        version_data = get_pypi_data(pypi_data['info']['name'], version=version)
        version = version_data.get('info', {}).get('version')
        if version is None:
            return None

    if lt:
        releases = [(r, rd[-1]['upload_time_iso_8601']) for r, rd in releases.items() if rd]
        releases = sorted(releases, key=lambda x: x[1], reverse=True)
        releases = [r for r, rd in releases]
        idx = releases.index(version)
        if idx < len(releases) - 1:
            return releases[idx + 1]
    return version


def get_version_release_dates(name, version, version_lt):
    pypi_data = get_pypi_data(name)
    if not pypi_data:
        return None, None

    releases = pypi_data['releases']
    latest_version = pypi_data['info']['version']
    if version_lt:
        version = get_version(pypi_data, version_lt, lt=True)

    version = get_version(pypi_data, version)
    if version is None:
        return None, None

    latest_version_date = releases[latest_version][-1]['upload_time_iso_8601']
    latest_version_date = datetime.datetime.strptime(latest_version_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    if version not in releases:
        return latest_version_date, latest_version_date

    version_date = releases[version][-1]['upload_time_iso_8601']
    version_date = datetime.datetime.strptime(version_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return version_date, latest_version_date


def get_lib_days(name, version, version_lt):
    cr, lr = get_version_release_dates(name, version, version_lt)
    return (lr - cr).days if cr else 0
