
### tkinter

tkinter is the python binding to the tcl/tk UI toolkit.
It can be a little tricky to configure.

1) To see if it is already installed and configured:
```console
$ python

>>> import tkinter
```
If you do not get an error then you can ignore the rest of the section

2) Install library
(Working on a mac)
```console
$ brew install python-tk
```

3) Rebuild python
(Using pyenv)

I use poetry for virtualenvs which point to the pyenv pythons

```console
➜  ~ pyenv versions
  system
  3.9.9
* 3.11.1 (set by /Users/ianmcallister/.pyenv/version)
➜  ~ pyenv uninstall 3.11.1
➜  ~ pyenv install 3.11.1
```

The reinstall builds the required links to the just install tkinter library

### Poetry

The environment is specified and managed with poetry.

You might need to install poetry
```console
➜  ~ brew install poetry
```

After cloning the repo use poetry to build the virtualenv
```console
➜  ~ poetry update

➜  ~ poetry env info

Virtualenv
Python:         3.11.1
Implementation: CPython
Path:           /Users/ianmcallister/Library/Caches/pypoetry/virtualenvs/theo-Ad0R6X59-py3.11
Executable:     /Users/ianmcallister/Library/Caches/pypoetry/virtualenvs/theo-Ad0R6X59-py3.11/bin/python
Valid:          True

System
Platform:   darwin
OS:         posix
Python:     3.11.1
Path:       /Users/ianmcallister/.pyenv/versions/3.11.1
Executable: /Users/ianmcallister/.pyenv/versions/3.11.1/bin/python3.11

```

This should show the link to the python version that is configured for tkinter
Now you can launch jupyter lab
```console
➜  ~ poetry run jupyter lab
```
