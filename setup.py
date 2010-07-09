import os
from distutils.core import setup

package_dirs = ('nomadblog', 'single_blog_example', 'multiple_blogs_example')

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
for package_dir in package_dirs:
    for dirpath, dirnames, filenames in os.walk(package_dir):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if '__init__.py' in filenames:
            packages.append('.'.join(fullsplit(dirpath)))
        elif filenames:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

doc_dir = os.path.join(os.path.dirname(__file__), 'docs')
long_desc_file = os.path.join(doc_dir, 'overview.rst')
version_num = __import__('nomadblog').__version__ 

setup(
    name='django-nomadblog',
    version=version_num,
    description='A minimalist Django blogging system.',
    long_description=open(long_desc_file).read(),
    author='Hector Garcia',
    author_email='hector@nomadblue.com',
    url='http://nomadblue.com/projects/django-nomadblog/',
    download_url='http://bitbucket.org/nabucosound/django-nomadblog/downloads/django-nomadblog-%s.tar.gz' % version_num,
    packages=packages,
    data_files=data_files,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
