#!/bin/sh
set -xe

if test -n "$HAL_PKG"; then
    HAL_LIBS="$(pkg-config --libs ${HAL_PKG})"
    L_RTAPI_MATH="$(pkg-config --variable lib_rtapi_math ${HAL_PKG})"
    L_HAL="$(pkg-config --variable lib_hal ${HAL_PKG})"
fi

g++ -o use-rs274 use-rs274.cc \
    -Wall -Wextra -Wno-return-type -Wno-unused-parameter \
    -I $HEADERS -I $INCLUDEPY -L $LIBDIR -Wl,-rpath,$LIBDIR -lrs274 \
    $HAL_LIBS $L_RTAPI_MATH $L_HAL
LD_BIND_NOW=YesPlease ./use-rs274
