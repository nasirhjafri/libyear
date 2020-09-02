#!/usr/bin/env python
import argparse

from prettytable import PrettyTable

from libyear.pypi import get_lib_days, get_no_of_releases
from libyear.utils import load_requirements, get_requirement_files, get_requirement_name_and_version


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help="Requirements file/path", action='store')
    parser.add_argument('--sort', help="Sort by years behind, in descending order", action='store_true')
    args = parser.parse_args()
    requirements = set()
    for req_file in get_requirement_files(args.r):
        requirements.update(load_requirements(req_file))

    pt = PrettyTable()
    pt.field_names = ['Library', 'Current Version', 'Latest Version', 'Libyears behind']
    total_days = 0
    
    for req in requirements:
        name, version, version_lt = get_requirement_name_and_version(req)
        if not name:
            continue

        if not version and not version_lt:
            continue
        
        v, lv, days = get_lib_days(name, version, version_lt)
        if v and days > 0:
            pt.add_row([name, v, lv, str(round(days / 365, 2))])
        total_days += days

    if args.sort:
        pt.sortby = 'Libyears behind'
        pt.reversesort = True

    if total_days == 0:
        print("Your system is up-to-date!")
    else:
        print(pt)
        print("Your system is %s libyears behind" % str(round(total_days / 365, 2)))
        


if __name__ == "__main__":
    main()
