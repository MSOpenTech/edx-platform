"""Setup for File Storage XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='xblock-file-storage',
    version='0.1',
    description='File Storage XBlock',   # TODO: write a better description.
    packages=[
        'onedrive',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils',
    ],
    dependency_links=[
        'http://github.com/edx-solutions/xblock-utils/tarball/master#egg=xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'onedrive = onedrive:OneDriveDocumentBlock',
        ]
    },
    package_data=package_data("onedrive", ["static", "templates", "public"]),
)
