#!/bin/sh
set -xe 
CPPFLAGS=$(pkg-config --silence-errors --cflags libtirpc)
if test -n "$HAL_PKG"; then
    CFLAGS="$(pkg-config --cflags ${HAL_PKG})"
fi
for i in $HEADERS/*.h; do
    case $i in
    */rtapi_app.h) continue ;;
    esac
    gcc ${CPPFLAGS} ${CFLAGS} -DULAPI -I$HEADERS -E -x c $i > /dev/null
done
for i in $HEADERS/*.h $HEADERS/*.hh; do
    case $i in
    */rtapi_app.h) continue ;;
    */interp_internal.hh) continue ;;
    esac
    if g++ ${CPPFLAGS} ${CFLAGS} -std=c++11 -S -o /dev/null -xcxx /dev/null > /dev/null 2>&1; then
        ELEVEN=-std=c++11
    else
        ELEVEN=-std=c++0x
    fi
    g++ ${CPPFLAGS} ${CFLAGS} $ELEVEN -DULAPI -I$HEADERS -E -x c++ $i > /dev/null
done
