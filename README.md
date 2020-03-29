Simple GTK 3 application to remove seperating characters from MAC addresses


**To build and install this program for single user:**

* `./autogen.sh --prefix=$HOME/.local`
* `make install`

**To build and install this program system wide:**

* `./autogen.sh`
* `sudo make install`

-------------
* Running the first line above creates the following files:
	* aclocal.m4
	* autom4te.cache
	* config.log
	* config.status
	* configure
	* macclean.desktop
	* install-sh
	* missing
	* Makefile.in
	* Makefile

Running "make install", installs the application in `$HOME/.local/bin`
and installs the macclean.desktop file in `$HOME/.local/share/applications`
or `/usr/local/bin and /usr/local/share/applications` for system wide installs.

You can now run the application by typing "MacClean" in the Overview.

----------------
**To uninstall, type:**

`make uninstall`
or
`sudo make unstinall` for system wide installs

----------------
**To create a tarball type:**

`make distcheck`

This will create macclean-1.0.tar.xz
