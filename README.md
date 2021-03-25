# Plone 5 buildout (python3)#

[![Build Status](https://travis-ci.org/RedTurtle/deployments.buildout.plone.png?branch=master)](https://travis-ci.org/RedTurtle/deployments.buildout.plone)

## Introduction ##
This is the a very basic buildout template to run Plone.
It is designed to make developer life easier.

## I am feeling lucky! ##
Lucky people read the documentation,
anyway if you have a local copy of this buildout,
try to run this command:
```bash
./.imfeelinglucky.sh
```

## For the impatients ##
Make a symlink to the file you want to use (e.g. `development.cfg`)
and start the buildout:
```bash
virtualenv --no-site-packages -p `which python3.7` .
. bin/activate
pip install -r requirements.txt
ln -s profiles/development.cfg buildout.cfg
buildout
```

## For volto users ##
If you need to develop a [Volto](https://github.com/plone/volto) project, you 
probably need to handle CORS. You can do this through a profile file, extending 
config/volto.cfg. E.g. in profiles/development.cfg you can do:

```
[buildout]
extends =
    config/development.cfg
    config/volto.cfg
```

Don't forget you also need to use collective.folderishtypes so extend your 
buildout with it:
```
eggs +=
    ${plone:eggs}
    collective.folderishtypes
```
or put this package in your dependencies

## Before you start ##
Probably you may want to set up your system and configure some parameters!
Don't forget to read the full documentation.

### Requirements ###
You may want to install this to get this buildout working:
```bash
# python stuff
apt-get install python-dev python-virtualenv libxml2-dev libxslt1-dev
# version control stuff
apt-get install git subversion
# other stuff
apt-get install libjpeg62-turbo-dev poppler-utils  wv libgeos-c1v5
```

Those commands are for Debian like system.
You should adapt those commands for your system (if needed).

## FAQ ##
#### Q: How can I clone this buildout? ####
__A:__ This buildout is meant to be a starting skeleton for a project.
You should download this buildout by visiting the
[dedicated github page](https://github.com/RedTurtle/deployments.buildout.plone).

There you can click the zip button.
Uncompress the downloaded zip file in the directory of your choice.
You may want to add this directory to the version control system of your
choice.

#### Q: How can I change the Plone version? ####
__A:__ In the file `config/base.cfg` you may can control the plone version by changing the
__extends__ and __find-links__ variables:
```cfg
extends =
    http://dist.plone.org/release/5.1.5/versions.cfg
    ...

find-links =
    http://dist.plone.org/release/5.1.5
    ...
```

__Tip__: unpin the versions in `versions/base.cfg`
to get the latest versions for your dependencies.
After a succesfull buildout repin them.

#### <a id="faq-egg"></a> Q: I have to add a new egg to my Plone site. What should I do? ####
__A:__ Customize the __eggs__ and (if needed) the __zcml__ variable in the **[plone]** section (a
good place is `config/base.cfg`), e.g:

```cfg
[plone]
eggs=
    ...
    my.egg
zcml=
    ...
    my.egg
```

#### Q: I want to develop my new package. What should I do? ####
- __A:__ Customize the `[sources]` section in `config/development.cfg` to include your code in the buildout:

```cfg
[sources]
collective.developermanual = git git://github.com/collective/collective.developermanual.git
```

- Add the egg to your Plone site (see the [dedicated FAQ](#faq-egg ))
- Relaunch your buildout.

#### Q: I want include a package from a private repository. What should I do? ####
- __A:__ Don't do it, use the folder pypi-local in the root of your buildout folder instead!

#### Q: I am Danny Developer. I want to include a debugging package nobody else wants to use. What should I do? ####
- __A:__ Create your own __profile__, e.g.:

```bash
cp profiles/development.cfg profiles/danny.cfg
ln -sf profiles/danny.cfg buildout.cfg
```

- Add a section like this to `profiles/danny.cfg`:
```cfg
[plone]
eggs+=
    danny.debugtools
```
- __If__ you need to checkout the package with mr.developer.

```cfg
[sources]
danny.debugtools = git git://github.com/dannydeveloper/danny.debugtools.git
```
- Relaunch your buildout.

#### Q: I am Danny Developer. I want to customize the instance port. What should I do? ####
- __A:__ Create your own __profile__, e.g.:

```bash
cp profiles/development.cfg profiles/danny.cfg
ln -sf profiles/danny.cfg buildout.cfg
```

- Add a section like this to `profiles/danny.cfg`:
```cfg
[instance]
http-address=9090
```

#### Q: I am Rick Releaser. I want to deploy this buildout on the server matrix.nohost.com. Of course I have to customize ports, users and so on. What should I do? ####
- __A:__ Create a dedicate __profile__ for this server, e.g.:

```bash
cp profiles/production.cfg profiles/matrix.cfg
ln -sf profiles/matrix.cfg buildout.cfg
```

- Add a section like this to `profiles/matrix.cfg`:

```cfg
[config]
zeo-address = 9010
instance1-address = 9001
debuginstance-address = 9000
system-user = plone
```

#### Q: How can I add an instance? ####
__A:__ In 'config/base.cfg' you can find, commented,
the configuration for `instance2`.
Uncomment it to get two instance.

Add also port number to [config] section.

Copy and adjust the numbers for more.

#### Q: I want supervisor, come on! Where is it? ####
__A:__ This buildout wants to be as small as possibile.
Integrate this buildout with
https://github.com/RedTurtle/deployments.buildout.production
if you need supervisor.

#### Q: I have to pin versions! What should I do? ####
__A:__ Modify `versions/base.cfg` unless you are doing for particular purposes.
In this case it is better to customize those versions in a dedicated profile.

## Tips ##

#### Virtualenv ####
Using a virtualenv is a good idea:
```bash
# NOTE: --no-site-packages is the default behaviour of the newer virtualenv
#       you might remove this parameter if you get an error
virtualenv --no-site-packages -p /usr/bin/python2.7 .
. bin/activate
```

#### mr.developer vs filesystem packages ####
If you want [mr.developer](https://pypi.python.org/pypi/mr.developer)
to use a folder that is not yet versioned
(e.g. because you still have to make an initial import),
you can use the __fs__ repository type:
```cfg
[sources]
still.to.import = fs still.to.import
```
By default paths are relative to buildout `src` folder.

## Rationale ##
This buildout was designed with these goals:
- cut down the time needed for the developers to set up a working enviroment
- avoid proliferation of configuration files
- to serve a Plone site without pretending to do much more

### Profiles ###
In the directory `./profiles` you will find configuration files
that work __if and only if__ they are symlinked in the root of the buildout.

We want profile files to live there to avoid pollution on the already crowded
buildout directory.

__You shouldn't use directly configuration files
that are stored in `config` folder.__

### The provided configuration files ###
Beneath is the list of available configurations:

#### development.cfg ####
This is what the developer wants!
Gives you a standalone Plone instance (no ZEO).
As usual you can launch it with:
```bash
./bin/instance fg
2013-03-22 13:58:39 INFO ZServer HTTP server started at Fri Mar 22 13:58:39 2013
Hostname: 0.0.0.0
Port: 8080
2013-03-22 13:58:44 INFO Zope Ready to handle requests
```
Adds to the buildout development scripts (`test`) and to plone some
products (`plone.reload` and `stxnext.pdb`).
Some other are suggested (commented) In the `profiles/development.cfg` file.
Ask for new stuff if you want (`sauna.reload`, `plone.app.debugtoolbar`, ...).

#### production.cfg ####
This is what you want for a production system.

Using `production.cfg` you will install the services:
- zeoserver
- instance1
- debuginstance

the management scripts:
- bin/zeopack
- bin/repozo

the logrotate machinery:
- etc/logorate.conf
- bin/postrotate.sh

##### Log rotation #####
The logrotation is handled externally from Zope by choice.
This allows at any time to use the system logrotate capabilities.
Logrotate are automaticaaly installed as a cronjob via a zc.buildout recipe
in config/production.cfg and config/staging.cfg

```

##### munin #####
`production.cfg` will provide you a script to deploy (if needed)
symlinks for munin.zope.
To install the munin plugins you can run:
```bash
sudo make install_munin

##### ZopeHealthWatcher #####

Remember to customize the `custom.py` file:
```bash
vi eggs/ZopeHealthWatcher*.egg/Products/ZopeHealthWatcher/custom.py
```

Then use it like this:
```bash
bin/zope_health_watcher http://localhost:8080
```

Or visit http://localhost:8080/manage_zhw?the_secret_you_put_in_custom.py
