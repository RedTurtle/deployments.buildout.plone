Plone 4 buildout
================

Introduction
------------
This is the a very basic buildout template

Requirements
------------
You may want to install this to get this buildout working:
```
# python stuff
apt-get install python-dev python-virtualenv
# version control stuff
apt-get install git subversion
# other stuff
apt-get install libjpeg8-dev poppler-utils  wv libgeos-c1
```

Installation
------------
In the file base.cfg there is a section called [config] that sets the variable
plone_version, e.g::
```
[config]
plone_version = 4.2.4
```

You may want to change this, before starting.

Using a virtualenv is a good idea:
```

# NOTE: --no-site-packages is the default behaviour of the newer virtualenv
#       you might remove this parameter if you get an error
virtualenv --no-site-packages -p /usr/bin/python2.7 .
. bin/activate
```

Then symlink the file you want to use (e.g. development.cfg) and start the buildout:
```
ln -s development.cfg buildout.cfg
python2.7 bootstrap.py
./bin/buildout
```

Add additional eggs to Plone
----------------------------
Customize the eggs, and *optionally* the zcml, variable in the plone section, e.g:
```
[plone]
eggs+=
    my.egg
zcml+=
    my.egg
```

Add development eggs to Plone
-----------------------------
Customize the [sources] section in development.cfg adding your checkouts, e.g:
```
[sources]
collective.developermanual = git git://github.com/collective/collective.developermanual.git
```

Note
----
