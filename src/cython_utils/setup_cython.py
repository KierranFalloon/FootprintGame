from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("c_utils.pyx", annotate=True, compiler_directives={'language_level' : "3"})
)
