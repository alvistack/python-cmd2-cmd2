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

The developers toolbox
----------------------

![system schema](https://github.com/python-cmd2/cmd2/blob/README_facelift/.github/images/graph.drawio.png)


When creating solutions developers have no shortage of tools in the belt when it comes to rich and smart user interfaces. `cmd2` deftly fills the niche between high [ease of command discovery](https://clig.dev/#ease-of-discovery) and smart workflow automation systems. The above graph is over simplified helps to illustrate when one should reach for cmd2 as the right choice. CLIs have long been the go to pick for those concerned with automation. System administrators have long been duct taping together precarious workflows based on a menagerie of simple command line tools created by strangers on github and the guy down the hall. When CLIs become significantly complex the ease of discoverability tends to fade quickly. Web and GUIs on the other hand are first in class when allowing users to easily discover functionality. The price we pay for beautifully colored displays is it is exceedingly difficult to aggregate many of these applications into larger systems.

With cmd2 you can have the best of both worlds. Application designers can easily create complex applications and rely on the cmd2 library to offer effortless user facing help and extensive tab completion. When users have become comfortable with functionality cmd2 turns into a feature rich library enabling a smooth transition to full automation. If designed with enough forethought, a well implemented cmd2 application can serve as a boutique workflow tool. `cmd2` pulls off this flexibility based on two pillars of philosophy.

Philosophy
-------------

<a href="https://imgflip.com/i/63h03x"><img src="https://i.imgflip.com/63h03x.jpg" title="made at imgflip.com"/></a><div><a href="https://imgflip.com/memegenerator"></a></div>


Deep extensive tab completion and help text generation based on the argparse library create the first pillar of 'ease of command discovery'. The following is a list of features in this category.

- Great tab completion of commands, subcommands, file system paths, and shell commands.
- Custom tab completion for user designed commands via simple function overloading.
- Tab completion from `persistent_history_file` sources added with very little friction.
- Automatic tab completion of `argparse` flags and optional arguments.
- Path completion easily enabled.
- When all else fails, custom tab completion based on `choices_provider` can fill any gaps.


cmd2 creates the second pillar of 'ease of transition to automation' through alias/macro creation, command line argument parsing and execution of cmd2 scripting.

- Flexible alias and macro creation for quick abstraction of commands.
- Text file scripting of your application with `run_script` (`@`) and `_relative_run_script` (`@@`)
- Powerful and flexible built-in Python scripting of your application using the `run_pyscript` command
- Transcripts for use with built-in regression can be automatically generated from `history -t` or `run_script -t`


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

| Application Name                                                | Description                                                                                                                     |   |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---|
| [Jok3r](http://www.jok3r-framework.com)                         | Network & Web Pentest Automation Framework                                                                                      |   |
| [CephFS Shell](https://github.com/ceph/ceph)                    | [Ceph](https://ceph.com/) is a distributed object, block, and file storage platform                                             |   |
| [psiTurk](https://psiturk.org)                                  | An open platform for science on Amazon Mechanical Turk                                                                          |   |
| [Poseidon](https://github.com/CyberReboot/poseidon)             | Leverages software-defined networks (SDNs) to acquire and then feed network traffic to a number of machine learning techniques. |   |
| [Unipacker](https://github.com/unipacker/unipacker)             | Automatic and platform-independent unpacker for Windows binaries based on emulation                                             |   |
| [tomcatmanager](https://github.com/tomcatmanager/tomcatmanager) | A command line tool and python library for managing a tomcat server                                                             |   |
| [Expliot](https://gitlab.com/expliot_framework/expliot)         | Internet of Things (IoT) exploitation framework                                                                                 |   |
| [mptcpanalyzer]()                                               | Tool to help analyze mptcp pcaps                                                                                                |   |
| [clanvas](https://github.com/marklalor/clanvas)                 | Command-line client for Canvas by Instructure                                                                                   |   |


Possibly defunct but still good examples

* [JSShell](https://github.com/Den1al/JSShell)
* [FLASHMINGO](https://github.com/fireeye/flashmingo) 
