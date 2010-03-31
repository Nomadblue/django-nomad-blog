import os
from distutils.core import setup

doc_dir = os.path.join(os.path.dirname(__file__), 'docs')
long_desc_file = os.path.join(doc_dir, 'overview.rst')

setup(
    name='django-nomadblog',
    version=__import__('nomadblog').__version__,
    description='A minimalist Django blogging system.',
    long_description=open(long_desc_file).read(),
    author='Hector Garcia',
    author_email='hector@nomadblue.com',
    url='http://nomadblue.com/projects/django-nomadblog/',
    download_url='http://bitbucket.org/nabucosound/django-nomadblog/downloads/django-nomadblog-0.2.tar.gz',
    packages=['nomadblog'],
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