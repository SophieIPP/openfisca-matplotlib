#! /usr/bin/env python
# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Matplotlib graphs for OpenFisca -- a versatile microsimulation free software"""


from setuptools import setup, find_packages


classifiers = """\
Development Status :: 2 - Pre-Alpha
Environment :: X11 Applications :: Qt
License :: OSI Approved :: GNU Affero General Public License v3
Operating System :: POSIX
Programming Language :: Python
Topic :: Scientific/Engineering :: Information Analysis
"""

doc_lines = __doc__.split('\n')


setup(
    name = 'OpenFisca-Matplotlib',
    version = '0.4dev',

    author = 'OpenFisca Team',
    author_email = 'contact@openfisca.fr',
    classifiers = [classifier for classifier in classifiers.split('\n') if classifier],
    description = doc_lines[0],
    keywords = 'benefit microsimulation social tax',
    license = 'http://www.fsf.org/licensing/licenses/agpl-3.0.html',
    long_description = '\n'.join(doc_lines[2:]),
    url = 'https://github.com/openfisca/openfisca-matplotlib',

    include_package_data = True,
    install_requires = [
        'OpenFisca-Core >= 0.4dev',
        ],
    packages = find_packages(),
    message_extractors = {
        'openfisca_matplotlib': [
            ('**.py', 'python', None),
            ],
        },
    zip_safe = False,
    )
