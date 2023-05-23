from setuptools import setup, find_packages

version = '1.1.1'

setup(name='collective.shariff',
      version=version,
      description="Implement shariff - social media buttons with privacy",
      long_description='\n\n'.join([
          open("README.rst").read(),
          open("CHANGES.rst").read(),
      ]),
      long_description_content_type='text/x-rst',
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: Addon",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
      ],
      keywords='Python Plone Addon shariff heise',
      author='petschki',
      author_email='peter.mathis@kominat.at',
      url='https://github.com/collective/collective.shariff',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      python_requires=">=2.7,<3",
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
