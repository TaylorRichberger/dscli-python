# Copyright © 2017 Absolute Performance Inc <csteam@absolute-performance.com>.
# All rights reserved.
# This is proprietary software.
# No warranty, explicit or implicit, provided.

.PHONY: all wheel tag clean

all: clean wheel

wheel: setup.py
	PYTHONPATH="$(shell pwd)" ./setup.py bdist_wheel

tag:
	git tag -s '$(shell PYTHONPATH="$(pwd)" python3.5 -c 'import dscli; print(dscli.__version__)')'

clean:
	git clean -xfd
