from setuptools import setup, find_packages

setup(
    name='django-nomadblog',
    version=__import__('nomadblog').__version__,
    description='A minimalist Django blogging system.',
    long_description=open('docs/overview.rst').read(),
    author='Hector Garcia',
    author_email='hector@nomadblue.com',
    url='http://bitbucket.org/nabucosound/django-nomadblog/',
    packages=find_packages(),
    zip_safe=False,
    package_dir={'nomadblog': 'nomadblog'},
    classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Framework :: Django',
    ]
)
