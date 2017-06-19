"""Public API

Anything that is not defined here is **internal** and
unreliable for external use.

Motivation for api.py:
    Storing the API in a module, as opposed to in __init__.py, enables
    use of it internally.

    For example, from `pipeline.py`:
        >> from . import api
        >> api.do_this()

    The important bit is avoiding circular dependencies, where api.py
    is calling upon a module which in turn calls upon api.py.

"""

from . import schema

from .pipeline import (
    install,
    uninstall,

    Loader,
    Creator,
    discover,

    register_root,
    register_host,
    register_format,
    register_plugin_path,
    register_plugin,

    registered_host,
    registered_plugin_paths,
    registered_root,

    deregister_plugin,
    deregister_plugin_path,
    deregister_format,
)

from .lib import (
    format_staging_dir,
    format_version,

    time,

    find_latest_version,
    parse_version,
    logger,
)


__all__ = [
    "install",
    "uninstall",

    "schema",

    "Loader",
    "Creator",
    "discover",

    "register_host",
    "register_format",
    "register_plugin_path",
    "register_plugin",
    "register_root",

    "registered_root",
    "registered_plugin_paths",
    "registered_host",

    "deregister_plugin",
    "deregister_plugin_path",
    "deregister_format",

    "format_staging_dir",
    "format_version",

    "find_latest_version",
    "parse_version",
    "logger",

    "time",
]
