from distutils.core import setup

setup(
    name = "django-compositekey",
    version = "2.5.x-unstable",
    url = 'https://github.com/simone/django-compositekey',
    author = 'Simone Federici',
    author_email = 's.federici@gmail.com',
    description = 'Use Django with embedded database that have composite multicolumn primary key and multiple foreignkeys',
    data_files = ["AUTHORS"],
    package_dir={'': 'src'},
    packages = [
        "compositekey",
        "compositekey.db",
        "compositekey.db.backends",
        "compositekey.db.backends.oracle",
        "compositekey.db.backends.postgresql_psycopg2",
        "compositekey.db.models",
        "compositekey.db.models.sql",
        "compositekey.db.models.fields",
        "compositekey.core",
        "compositekey.core.management",
        "compositekey.forms"
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)
