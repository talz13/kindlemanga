# Required Packages to Run kindlemanga #
  * [Python 2.6.4](http://www.python.org/download/)
  * [UnRAR2 0.96](http://code.google.com/p/py-unrar2/)
  * [PIL-1.1.6](http://www.pythonware.com/products/pil/)
  * [wxPython 2.8.10.1](http://www.wxpython.org/)

## Installation ##
  1. Install Python 2.6
  1. Install UnRAR2 `*`
  1. Install PIL `*`
  1. Install wxPython `*`

## Win-x64 Users ##
`*` If you are using a 64 bit version of Windows, follow the instructions here if you are having problems with the python module installers not finding the Python path.:
> http://effbot.slinkset.com/items/Adding_Python_Information_to_the_Windows_Registry
You can download and use a sample registry file using the default install paths for Python 2.6.5 to fix this issue:
  * http://kindlemanga.googlecode.com/files/python.reg

Also, PIL seems to have issues, as installed with the 32bit installer.  Please check here for a 64 bit version of PIL:
  * http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil


# Suggested Packages to Build kindlemanga #

  * [Java JDK](http://java.sun.com/javase/downloads/widget/jdk6.jsp)
  * [Netbeans 6.8](http://netbeans.org/downloads/index.html)
  * wxFormBuilder >= 3.1.67-beta and wxAdditions\_Plugin\_v1.08 (latest version can be found on: http://forum.wxformbuilder.org/)
  * [py2exe](http://www.py2exe.org/)

## Installation ##
  1. Install Java JDK
  1. Install Netbeans IDE
  1. Install wxFormBuilder
    * After installing wxFormBuilder, extract wxAdditions\_Plugin archive to the install folder, one of these locations:
      * C:\Program Files\wxFormBuilder\plugins
      * C:\Program Files (x86)\wxFormBuilder\plugins
  1. Install py2exe to package an exe using kindlemanga's setup.py