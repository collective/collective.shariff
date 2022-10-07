from setuptools import find_packages
from setuptools import setup


version = "3.0.0"

setup(
    name="collective.shariff",
    version=version,
    description="Implement shariff - social media buttons with privacy",
    long_description="\n\n".join(
        [
            open("README.rst").read(),
            open("CHANGES.rst").read(),
        ]
    ),
    long_description_content_type="text/x-rst",
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: Addon',
        'Framework :: Plone :: 6.0',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone social sharing shariff',
    author="petschki",
    author_email="peter.mathis@kominat.at",
    url="https://github.com/collective/collective.shariff",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["collective"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "plone.api>=1.5",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework",
            "robotframework-selenium2library",
        ]
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
