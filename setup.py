from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='collective.shariff',
      version=version,
      description="Implement shariff - social media buttons with privacy",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        ],
      keywords='',
      author='petschki',
      author_email='peter.mathis@kominat.at',
      url='https://github.com/collective/collective.shariff',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.api>=1.5',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
