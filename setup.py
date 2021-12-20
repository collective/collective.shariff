from setuptools import setup, find_packages

version = '1.1'

setup(name='collective.shariff',
      version=version,
      description="Implement shariff - social media buttons with privacy",
      long_description='\n\n'.join([
            open("README.rst").read(),
            open("docs/TODO.rst").read(),
            open("docs/CONTRIBUTORS.rst").read(),
            open("docs/HISTORY.rst").read(),
            ]),
      long_description_content_type='text/x-rst',
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
