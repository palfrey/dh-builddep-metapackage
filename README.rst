dh-builddep-metapackage
-----------------------

dh-builddep-metapackage builds build-dep metapackages in order to ease package
management for package rebuilders. In effect, it builds a <package
name>-builddep package that has no content, but depends on everything that the
existing package build-depends on. Most of this can be done with "apt-get
build-dep", but I find that I install random packages I need to rebuild
something, and then later on I'm wondering why I've got those installed. By
using dh-builddep-metapackage to create metapackages, I keep a record in the
package management about why I need a particular development package, and can
remove the dependant packages when I'm no longer working with the relevant
source package.

Standard usage is "dh-builddep-metapackage -b <package name>", which will create
the metapackage data and build the package for you using dpkg-buildpackage. A 
folder called "<package name>-<package version>" will be created in the current
local directory, and if an existing folder exists then dh-builddep-metapackage 
will refuse to overwrite it (unless you give the -o/--overwrite option).

Options:
  -h, --help            show this help message and exit
  -o, --overwrite       Overwrite existing destination folder
  -n NAME, --name=NAME  Maintainer name (Default: whatever you have in DEBNAME)
  -e EMAIL, --email=EMAIL
                        Maintainer email (Default: whatever you have in DEBEMAIL)
  -v VERSION, --version=VERSION
                        Use package with specific version (Default: Use
                        highest priority version)
  -b, --build           Build the package with dpkg-buildpackage
  -w, --working-directory
                        Use working directory as a source of package data.
                        Assumes we're in a folder with a 'debian' subdirectory

# vim: set textwidth=80:
