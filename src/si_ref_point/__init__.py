from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("si_ref_point")
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"
