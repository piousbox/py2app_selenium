
== Setup ==
From: https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
 pip install virtualenv
 virtualenv venv
 virtualenv venv --system-site-packages

 pip install selenium

 brew install tcl-tk
 # brew uninstall python
 # brew install python --with-tcl-tk
From: https://stackoverflow.com/questions/15884075/tkinter-in-a-virtualenv

== Build ==

For debugging:

 python setup.py py2app -A

For production:

 python setup.py py2app

== Run ==
 . venv/bin/activate
 ./dist/selenium_test.app/Contents/MacOS/selenium_test

