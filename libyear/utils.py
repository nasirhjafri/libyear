import os


def get_requirement_files(path_or_file):
    if os.path.isfile(path_or_file):
        yield path_or_file
        return
    for path, subdirs, files in os.walk(path_or_file):
        for name in files:
            yield os.path.join(path, name)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, or editable.
    """
    # Remove whitespace at the start/end of the line
    line = line.strip()

    # Skip blank lines, comments, and editable installs
    return not (
            line == '' or
            line.startswith('-r') or
            line.startswith('#') or
            line.startswith('-e') or
            line.startswith('git+')
    )


def load_requirements(requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.strip() for line in open(path).readlines()
            if is_requirement(line)
        )
    return list(requirements)
