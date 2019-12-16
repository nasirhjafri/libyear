[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/nasirhjafri/libyear/)
[![PyPI version fury.io](https://badge.fury.io/py/libyear.svg)](https://pypi.python.org/pypi/libyear/)
[![GitHub contributors](https://img.shields.io/github/contributors/nasirhjafri/libyear.svg)](https://GitHub.com/nasirhjafri/libyear/graphs/contributors/)


# libyear 

A **simple** measure of software dependency freshness. It is a **single number** telling you how up-to-date your dependencies are.

![Demo Image](./docs/demo.png)

## How to install
`pip install libyear`


## Usage
A single requirement file
`libyear -r requirements.txt`

A folder with requirement files
`libyear -r requirements/`

## Example output
```
libyear -r requirements.txt 
+-------------------------+-----------------+----------------+-----------------+
|         Library         | Current Version | Latest Version | Libyears behind |
+-------------------------+-----------------+----------------+-----------------+
|           pytz          |      2015.2     |     2019.3     |       4.54      |
|         urllib3         |      1.15.1     |     1.25.7     |       3.58      |
|         astroid         |      1.5.3      |     2.3.3      |       2.43      |
|          django         |     1.11.23     |      3.0       |       0.34      |
|      django-celery      |      3.2.1      |     3.3.1      |       2.54      |
|        httpretty        |      0.8.3      |     0.9.7      |       5.31      |
|         Pygments        |       1.6       |     2.5.2      |       6.81      |
|          flake8         |      3.6.0      |     3.7.9      |       1.01      |
|      django-waffle      |      0.14.0     |     0.18.0     |       1.66      |
|    requests_oauthlib    |      0.8.0      |     1.3.0      |       2.72      |
|   django-debug-toolbar  |       1.8       |      2.1       |       2.52      |
|         libsass         |      0.13.3     |     0.19.4     |       2.06      |
|     django-storages     |      1.6.6      |      1.8       |       1.65      |
|      edx-i18n-tools     |      0.4.2      |     0.5.0      |       2.02      |
|           six           |      1.10.0     |     1.13.0     |       4.08      |
|   djangorestframework   |      3.6.3      |     3.11.0     |       2.58      |
|          isort          |      4.2.15     |     4.3.21     |       2.05      |
|         futures         |      2.1.6      |     3.3.0      |       5.5       |
|          Pillow         |      2.7.0      |     6.2.1      |       4.8       |
| edx-django-release-util |      0.3.1      |     0.3.2      |       2.44      |
|      beautifulsoup4     |      4.6.0      |     4.8.1      |       2.42      |
|       mysqlclient       |   1.4.2.post1   |     1.4.6      |       0.77      |
|         newrelic        |    4.14.0.115   |   5.4.0.132    |       0.78      |
|          redis          |      2.10.6     |     3.3.11     |       2.16      |
|         oauthlib        |      2.1.0      |     3.1.0      |       1.21      |
|        django-ses       |      0.7.1      |     0.8.13     |       3.65      |
|           mock          |      1.3.0      |     3.0.5      |       3.79      |
|      django-hamlpy      |      1.1.1      |      1.2       |       1.52      |
|          bottle         |      0.12.9     |    0.12.18     |       4.1       |
|      pylint-django      |      0.7.2      |     2.0.13     |       3.44      |
|       user-agents       |      1.1.0      |      2.0       |       2.13      |
|          jsmin          |      2.2.1      |     2.2.2      |       1.15      |
|         Markdown        |       2.4       |     3.1.1      |       5.26      |
|         gunicorn        |      0.17.4     |     20.0.4     |       6.59      |
|         requests        |      2.18.4     |     2.22.0     |       1.75      |
|          pylint         |      1.7.2      |     2.4.4      |       2.39      |
+-------------------------+-----------------+----------------+-----------------+
Your system is 103.78 libyears behind
```

## Example 1
For example, a rails 5.0.0 dependency (released June 30, 2016) is roughly 1 libyear behind the 5.1.2 version (released June 26, 2017).

## Simpler is Better
There are obviously more nuanced ways to calculate dependency freshness. The advantage of this approach is its simplicity. You will be able to explain this calculation to your colleagues in about 30s.

## Example 2
If your system has two dependencies, the first one year old, the second three, then your system is four libyears out-of-date.

## A Healthy App
Apps below 10 libyears are considered to be healthy apps. We regularly rescue projects that are over 100 libyears behind.

## Etymology
"lib" is short for "library", the most common form of dependency.

## References
J. Cox, E. Bouwers, M. van Eekelen and J. Visser, Measuring Dependency Freshness in Software Systems. In Proceedings of the 37th International Conference on Software Engineering (ICSE 2015), May 2015 https://ericbouwers.github.io/papers/icse15.pdf
