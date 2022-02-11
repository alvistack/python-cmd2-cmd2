<h1 align="center">cmd2 : immersive interactive command line applications</h1>

[![Latest Version](https://img.shields.io/pypi/v/cmd2.svg?style=flat-square&label=latest%20stable%20version)](https://pypi.python.org/pypi/cmd2/)
[![GitHub Actions](https://github.com/python-cmd2/cmd2/workflows/CI/badge.svg)](https://github.com/python-cmd2/cmd2/actions?query=workflow%3ACI)
[![Azure Build status](https://python-cmd2.visualstudio.com/cmd2/_apis/build/status/python-cmd2.cmd2?branch=master)](https://python-cmd2.visualstudio.com/cmd2/_build/latest?definitionId=1&branch=master)
[![codecov](https://codecov.io/gh/python-cmd2/cmd2/branch/master/graph/badge.svg)](https://codecov.io/gh/python-cmd2/cmd2)
[![Documentation Status](https://readthedocs.org/projects/cmd2/badge/?version=latest)](http://cmd2.readthedocs.io/en/latest/?badge=latest)
<a href="https://discord.gg/RpVG6tk"><img src="https://img.shields.io/badge/chat-on%20discord-7289da.svg" alt="Chat"></a>


<p align="center">
  <a href="#main-features">Main Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#tutorials">Tutorials</a> •
  <a href="#projects-using-cmd2">Projects using cmd2</a> •
  <a href="#version-two-notes">Version 2.0 Notes</a>
</p>

[![Screenshot](cmd2.png)](https://youtu.be/DDU_JH6cFsA)

cmd2 is a tool for building interactive command line applications in Python. Its goal is to make it
quick and easy for developers to build feature-rich and user-friendly interactive command line
applications.  It provides a simple API which is an extension of Python's built-in
[cmd](https://docs.python.org/3/library/cmd.html) module.  cmd2 provides a wealth of features on top
of cmd to make your life easier and eliminates much of the boilerplate code which would be necessary
when using cmd.

Philosophy
-------------

<a href="https://imgflip.com/i/63h03x"><img src="https://i.imgflip.com/63h03x.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator"></a></div>


![system schema](https://github.com/python-cmd2/cmd2/blob/README_facelift/.github/images/graph.drawio.png)

Main Features
-------------

Tab complete all of the goodness
- Good tab completion of commands, subcommands, file system paths, and shell commands
- Top-notch tab completion capabilities which are easy to use but very powerful
- Can provide custom tab completion for the **foo** command by creating a **complete_foo** method
History and how it could be used for awesome tab completion
- Via optional `persistent_history_file` argument to `cmd2.Cmd` initializer
- `cmd2` in combination with `argparse` also provide several advanced capabilities for automatic tab completion
- Automatic tab completion of `argparse` flags when using one of the `cmd2` `argparse` decorators

I feel like these types of completion are important but they don't make sense unless you delve really deep into cmd2. 
- `basic_complete` helper method for tab completion against a list
- `path_complete` helper method provides flexible tab completion of file system paths
- `delimiter_complete` helper method for tab completion against a list but each match is split on a delimiter 
- `flag_based_complete` helper method for tab completion based on a particular flag preceding the token being completed
- `index_based_complete` helper method for tab completion based on a fixed position in the input string


Python scripting should be super highlighted
- Python scripting of your application with ``run_pyscript``


Transcripts are a great feature. Not sure if they are more useful for testing or for perhaps creating scripts...
- Built-in regression testing framework for your applications (transcript-based testing)
- Transcripts for use with built-in regression can be automatically generated from `history -t` or `run_script -t`
- Text file scripting of your application with `run_script` (`@`) and `_relative_run_script` (`@@`)
- Simple scripting using text files with one command + arguments per line
- Powerful and flexible built-in Python scripting of your application using the `run_pyscript` command
- Run arbitrary Python scripts within your `cmd2` application with the ability to also call custom `cmd2` commands


Not sure about these
- Macros, which are similar to aliases, but they can contain argument placeholders
- Ability to run commands at startup from an initialization script


Readline is useful but how many people actually remember to use it?
- Readline history using `<Ctrl>+r`, arrow keys, and other [Readline Shortcut keys](http://readline.kablamo.org/emacs.html)
- `cmd2` `history` command provides flexible and powerful search
- Searchable command history (`history` command and `<Ctrl>+r`) - optionally persistent


Installation
------------
On all operating systems, the latest stable version of `cmd2` can be installed using pip:

```bash
pip install -U cmd2
```

cmd2 works with Python 3.6+ on Windows, macOS, and Linux. It is pure Python code with few 3rd-party dependencies.

For information on other installation options, see
[Installation Instructions](https://cmd2.readthedocs.io/en/latest/overview/installation.html) in the cmd2
documentation.


Documentation
-------------
The latest documentation for cmd2 can be read online here: https://cmd2.readthedocs.io/en/latest/

It is available in HTML, PDF, and ePub formats.


The best way to learn the cmd2 api is to delve into the example applications located in source under examples.

Tutorials
---------

* PyOhio 2019 presentation: 
    * [video](https://www.youtube.com/watch?v=pebeWrTqIIw)
    * [slides](https://github.com/python-cmd2/talks/blob/master/PyOhio_2019/cmd2-PyOhio_2019.pdf)
    * [example code](https://github.com/python-cmd2/talks/tree/master/PyOhio_2019/examples)
* [Cookiecutter](https://github.com/cookiecutter/cookiecutter) Templates from community
    * Basic cookiecutter template for cmd2 application : https://github.com/jayrod/cookiecutter-python-cmd2
    * Advanced cookiecutter template with external plugin support : https://github.com/jayrod/cookiecutter-python-cmd2-ext-plug


Found a bug?
------------

If you think you've found a bug, please first read through the open [Issues](https://github.com/python-cmd2/cmd2/issues). If you're confident it's a new bug, go ahead and create a new GitHub issue. Be sure to include as much information as possible so we can reproduce the bug.  At a minimum, please state the following:

* ``cmd2`` version
* Python version
* OS name and version
* What you did to cause the bug to occur
* Include any traceback or error message associated with the bug


Projects using cmd2
-------------------------------

| Application Name                                                      | Description                                                                                                                     |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [Jok3r](http://www.jok3r-framework.com)                               | Network & Web Pentest Automation Framework                                                                                      |
| [CephFS Shell](http://docs.ceph.com/docs/master/cephfs/cephfs-shell/) | [Ceph](https://ceph.com/) is a distributed object, block, and file storage platform                                             |
| [JSShell](https://github.com/Den1al/JSShell)                          | An interactive multi-user web JavaScript shell.                                                                                 |
| [psiTurk](https://psiturk.org)                                        | An open platform for science on Amazon Mechanical Turk                                                                          |
| [Poseidon](https://github.com/CyberReboot/poseidon)                   | Leverages software-defined networks (SDNs) to acquire and then feed network traffic to a number of machine learning techniques. |
| [Unipacker](https://github.com/unipacker/unipacker)                   | Automatic and platform-independent unpacker for Windows binaries based on emulation                                             |
| [FLASHMINGO](https://github.com/fireeye/flashmingo)                   | Automatic analysis of SWF files based on some heuristics. Extensible via plugins.                                               |
| [tomcatmanager](https://github.com/tomcatmanager/tomcatmanager)       | A command line tool and python library for managing a tomcat server                                                             |
| [Expliot](https://gitlab.com/expliot_framework/expliot)               | Internet of Things (IoT) exploitation framework                                                                                 |
| [mptcpanalyzer](https://github.com/teto/mptcpanalyzer)                | Tool to help analyze mptcp pcaps                                                                                                |
| [clanvas](https://github.com/marklalor/clanvas)                       | Command-line client for Canvas by Instructure                                                                                   |


Version 2.0 Notes
-----------------
- Python 3.5 support ended
  - The last release of `cmd2` to support Python 3.5 was the 1.5.0 release on January 31, 2021.  Python 3.5 was
    [released](https://docs.python.org/3/whatsnew/3.5.html) on Sept. 13, 2015 and it reached
    [end-of-life](https://devguide.python.org/#status-of-python-branches) on September 5, 2020.
- `cmd2` 2.0 simplifies portions of the API and introduces new features. Many of these changes are not compatible with
  previous versions of `cmd2`. For assistance with porting your current `cmd2` application to version 2.0, see the
  [CHANGELOG](https://github.com/python-cmd2/cmd2/blob/master/CHANGELOG.md) for a description of each breaking
  change and enhancement.
 