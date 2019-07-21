#!/bin/sh
if test -n "$HAL_PKG"; then
    CFLAGS="$(pkg-config --cflags ${HAL_PKG})"
fi
gcc -O -I${HEADERS} test.c -o test -DULAPI -std=gnu99 $CFLAGS -pthread \
    || exit 1
./test; exitval=$?
rm -f test
exit $exitval
