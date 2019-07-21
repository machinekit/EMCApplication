#!/bin/sh
set -x
g++ -I${HEADERS} ${CFLAGS}\
    nml-position-logger.cc \
    -L ${LIBDIR} -lnml -llinuxcnc \
    -o /dev/null
