from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("int_part", ["int_part.pyx"])]

setup(
  name = 'int_part',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)

