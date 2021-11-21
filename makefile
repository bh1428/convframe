#
# makefile for convframe package
#

# Version: 2021.11.21

# Make targets:
#   upgrade_pip_tools     upgrade pip and the pip-tools package
#   upgrade_requirements  upgrade *requirements.txt files without installing
#   upgrade_venv          upgrade pip-tools, *requirements.txt and install packages
#   sync                  synchronize venv with *requirements.txt (default target)
#   info                  show list of installed packages in the venv
#   init                  initialize a new virtual environment
#   clean                 remove virtual environment
#   qt_designer           start QT Designer
#   run                   execute example template
#   build                 build package (.whl file)

# names (directories & files)
PACKAGE := convframe
VENV_DIR := venv
VENV_CLEAN_DIRS := .mypy_cache __pycache__
PRECLEAN_DIRS := build dist $(PACKAGE).egg-info
PRECLEAN_FILES :=
POSTCLEAN_DIRS := build $(PACKAGE).egg-info
POSTCLEAN_FILES :=
EXTRA_CLEAN_FILES := setup.py.bck

# binaries / executables
CMD := "C:\Windows\System32\cmd.exe"
PYTHON := "C:\Program Files\Python39\python.exe"
VENV := .\$(VENV_DIR)\Scripts
VENV_ACTIVATE := $(VENV)\activate.bat
VENV_PYTHON := $(VENV)\python.exe
PIP := $(VENV)\pip.exe
PIP_SYNC := $(VENV)\pip-sync.exe
PIP_COMPILE := $(VENV)\pip-compile.exe
PYSIDE2_UIC := $(VENV)\pyside2-uic.exe
PYSIDE2_RCC := $(VENV)\pyside2-rcc.exe
QT_DESIGNER := $(VENV_DIR)\Lib\site-packages\PySide2\designer.exe

all: build

.NOTPARALLEL:

init: $(VENV_ACTIVATE)

$(VENV_ACTIVATE):
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PYTHON) -m pip install pip --upgrade
	$(VENV_PYTHON) -m pip install pip-tools
    ifeq (,$(wildcard requirements.txt))
		$(PIP_COMPILE) requirements.in
    endif
    ifeq (,$(wildcard dev-requirements.txt))
		$(PIP_COMPILE) dev-requirements.in
    endif
	$(PIP_SYNC) dev-requirements.txt
	$(PIP) install -e .

requirements.txt: $(VENV_ACTIVATE) requirements.in
	$(PIP_COMPILE) requirements.in

dev-requirements.txt: $(VENV_ACTIVATE) dev-requirements.in requirements.txt
	$(PIP_COMPILE) dev-requirements.in

.PHONY: upgrade_pip_tools
upgrade_pip_tools: $(VENV_ACTIVATE)
	$(VENV_PYTHON) -m pip install pip --upgrade
	$(VENV_PYTHON) -m pip install pip-tools --upgrade

.PHONY: upgrade_requirements
upgrade_requirements: $(VENV_ACTIVATE)
	$(PIP_COMPILE) requirements.in --upgrade
	$(PIP_COMPILE) dev-requirements.in --upgrade

.PHONY: sync
sync: $(VENV_ACTIVATE) dev-requirements.txt
	$(PIP_SYNC) dev-requirements.txt
	$(PIP) install -e .

.PHONY: upgrade_venv
upgrade_venv: upgrade_pip_tools upgrade_requirements sync

.PHONY: info
info: $(VENV_ACTIVATE)
	$(PIP) list

.PHONY: clean
clean:
	$(CMD) /c "FOR %%F IN ($(VENV_DIR) $(VENV_CLEAN_DIRS)) DO IF EXIST %%F rmdir /q /s %%F"

.PHONY: qt_designer
qt_designer: $(VENV_ACTIVATE)
	$(QT_DESIGNER) ui/maindialog.ui

$(PACKAGE)/ui_maindialog.py: ui/maindialog.ui
	$(PYSIDE2_UIC) --from-imports -o $(PACKAGE)/ui_maindialog.py ui/maindialog.ui

$(PACKAGE)/maindialog_rc.py: maindialog.qrc images/python-icon.svg
	$(PYSIDE2_RCC) -o $(PACKAGE)/maindialog_rc.py maindialog.qrc

.PHONY: run
run: $(VENV_ACTIVATE)
	$(VENV_PYTHON) convframetemplate.py

.PHONY: build
build: $(VENV_ACTIVATE) $(PACKAGE)/ui_maindialog.py $(PACKAGE)/maindialog_rc.py
	$(CMD) /c "FOR %%F IN ($(PRECLEAN_DIRS)) DO IF EXIST %%F rmdir /q /s %%F"
	$(CMD) /c "FOR %%F IN ($(PRECLEAN_FILES)) DO IF EXIST %%F del %%F"
	$(VENV_PYTHON) setup.py bdist_wheel
	$(VENV_PYTHON) -c "import sys; import datetime; print(f'Python {sys.version}'); print(f'Build time: {datetime.datetime.now().astimezone()}\n')" > build_info.txt
	$(PIP) list >> build_info.txt
	$(CMD) /c copy build_info.txt dist
	$(CMD) /c "FOR %%F IN ($(POSTCLEAN_DIRS)) DO IF EXIST %%F rmdir /q /s %%F"
	$(CMD) /c "FOR %%F IN ($(POSTCLEAN_FILES)) DO IF EXIST %%F del %%F"
