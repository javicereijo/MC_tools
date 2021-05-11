#!/bin/sh
if test -z "$PYEPICS_LIBCA"; then
    MYLIB=$EPICS_BASE/lib/$EPICS_HOST_ARCH/libca.so
    if test -r "$MYLIB"; then
	PYEPICS_LIBCA=$MYLIB
	export PYEPICS_LIBCA
    fi
fi &&


/home/javiercereijogarcia/repos/MC_tools/IRIS/IRIS_slit_allaxes_SystemStartupSeq_lab.py
#/home/javiercereijogarcia/repos/MC_tools/IRIS/IRIS_slitSystemMoveGapAndPoistion_lab.py

