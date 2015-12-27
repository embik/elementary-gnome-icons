#!/bin/sh

set -e

autoreconf --force --install --symlink --warning=all

if test -z "${NOCONFIGURE}"; then
	set -x
	./configure --prefix=/usr "$@"
	make clean
fi
