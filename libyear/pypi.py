import requests


def get_pypi_data(name):
    """return a dictionary with pypi project data"""
    url = "https://pypi.org/pypi/%s/json" % name
    r = requests.get(url)
    if r.status_code < 400:
        return r.json()
    return {}
