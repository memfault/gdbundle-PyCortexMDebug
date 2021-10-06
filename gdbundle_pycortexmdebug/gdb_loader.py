def gdbundle_load():
    # the PyCortexMDebug package is embedded as a git submodule, because at the
    # time of this writing (2021-10-06), there is no pypi-deployed version of
    # PyCortexMDebug, and pypi packages cannot specify deps from sources other
    # than pypi (eg git)

    # due to this approach, we need to inject the search path for the submodule,
    # since without modifying it we can't include it as a subpackage.
    import sys, os

    yolo = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "gdbundle_pycortexmdebug", "cmdebug"
    )
    sys.path.append(yolo)

    from gdbundle_pycortexmdebug.cmdebug.cmdebug.svd_gdb import LoadSVD
    from gdbundle_pycortexmdebug.cmdebug.cmdebug.dwt_gdb import DWT

    LoadSVD()
    DWT()
