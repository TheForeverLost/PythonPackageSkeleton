# PythonPackageSkeleton

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)[![PyPi Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)

A template repo to act as skeleton for any python package

### Installation & Usage

1. Clone the repository or [use this template](https://github.blog/2019-06-06-generate-new-repositories-with-repository-templates/) when creating repository

   ```bash
   git clone https://github.com/TheForeverLost/PythonPackageSkeleton.git
   cd PythonPackageSkeleton
   ```

2. install setuptools wheel to latest version

   ```bash
   python3 -m pip install --user --upgrade setuptools wheel
   ```

3. A [makefile](https://github.com/TheForeverLost/PythonPackageSkeleton/blob/master/makefile) has been setup to automate all your commands
   update **setup.py** with your project details rename the sample folder to `<your package name>` and run 

   ```bash
   make init
   ```

   make sure your dependencies are well setup in setup.py install_requires and requirements.txt 
   check  [this article](https://packaging.python.org/discussions/install-requires-vs-requirements/) for further clarification

4. This particular uses pytest for testing so once you have added programs in your package add tests in *tests/* and run

   ```bash
   make test
   ```

5.  You can use the dist command to build distributables

   ```bash
   make dist
   ```

6.  Commands have been added for test deployment to testpypi as well as pypi

   ```bash
   make testdeploy
   ```

   You'll need a pypi account before you deploy it to pypi

   ```bash
   make deploy
   ```

   

