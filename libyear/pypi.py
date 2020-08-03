from distutils.version import LooseVersion

import dateutil.parser
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


def clean_version(version):
    version = [v for v in version if v.isdigit() or v == '.']
    return ''.join(version)


def get_version(pypi_data, version, lt=False):
    if not version:
        return None

    orig_ver = version
    releases = pypi_data['releases']
    if version not in releases:
        version_data = get_pypi_data(pypi_data['info']['name'], version=version)
        version = version_data.get('info', {}).get('version')
    if lt:
        releases = [(r, rd[-1]['upload_time_iso_8601']) for r, rd in releases.items() if rd]
        releases = sorted(releases, key=lambda x: x[1], reverse=True)
        releases = [r for r, rd in releases]
        if version is None:
            curr_ver = LooseVersion(clean_version(orig_ver))
            releases_float = [clean_version(r) for r in releases]
            releases_float = [r for r in releases_float if LooseVersion(r) >= curr_ver]
            return releases[len(releases_float)]

        idx = releases.index(version)
        if idx < len(releases) - 1:
            return releases[idx + 1]
    return version

def get_no_of_releases(name, version):
    pypi_data = get_pypi_data(name)
    if not pypi_data:
        return None, None, None, None

    releases = pypi_data['releases']
    
    return (len(releases)-list(releases).index(version))

def get_version_release_dates(name, version, version_lt):
    pypi_data = get_pypi_data(name)
    if not pypi_data:
        return None, None, None, None

    releases = pypi_data['releases']
    latest_version = pypi_data['info']['version']
    if version_lt:
        version = get_version(pypi_data, version_lt, lt=True)

    version = get_version(pypi_data, version)
    if version is None:
        return None, None, None, None

    try:
        latest_version_date = releases[latest_version][-1]['upload_time_iso_8601']
    except IndexError:
        print(f'Latest version of {name!r} has no upload time.')
        return None, None, None, None

    latest_version_date = dateutil.parser.parse(latest_version_date)
    if version not in releases:
        return None, latest_version_date, latest_version, latest_version_date

    try:
        version_date = releases[version][-1]['upload_time_iso_8601']
    except IndexError:
        print(f'Used release of {name}=={version} has no upload time.')
        return None, None, None, None

    version_date = dateutil.parser.parse(version_date)
    return version, version_date, latest_version, latest_version_date


def get_lib_days(name, version, version_lt):
    v, cr, lv, lr = get_version_release_dates(name, version, version_lt)
    libdays = (lr - cr).days if cr else 0
    return v, lv, libdays
