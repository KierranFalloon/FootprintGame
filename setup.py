from setuptools import setup, Extension
import sys

with open("requirements.txt") as f:
      requirements = f.read().splitlines()

try:
   from Cython.Build import cythonize
   extensions = [Extension('src.cython_utils.c_utils', sources=['src/cython_utils/c_utils.pyx'])]
   extensions = cythonize(extensions,
                  compiler_directives={
                     'language_level' : "3"}
                  )
except ImportError:
   extensions = [Extension('src.cython_utils.c_utils', sources=['src/cython_utils/c_utils.c'])]

with open('setup_log.txt', 'w+') as log_file:

   sys.stdout = log_file
   sys.stderr = log_file

   setup(
      name='Pokemon Footprint Game',
      version='1.0',
      install_requires=requirements,
      description='The Pokémon Footprint (Sentry duty) game, extended for 8 generations',
      author='Kierran Falloon',
      author_email='kgwfalloon@gmail.com',
      url = 'https://github.com/KierranFalloon/FootprintGame',
      ext_modules = extensions
   )

with open('setup_log.txt', 'r') as log_file:
   sys.stdout.write(log_file.read())