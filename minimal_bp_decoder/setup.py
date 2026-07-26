from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import scipy
import os
import sys

cpp_include = os.path.abspath('src_cpp')

if sys.platform == 'win32':
    compile_args = ['/std:c++17']
else:
    compile_args = ['-std=c++17']

ext_modules = [
    Extension(
        'myldpc.bp_decoder._bp_decoder',
        sources=[
            'src_python/myldpc/bp_decoder/_bp_decoder.pyx',
        ],
        include_dirs=[
            cpp_include,
            np.get_include(),
            os.path.join(os.path.dirname(scipy.__file__), 'include'),
            'src_python/myldpc/bp_decoder',
            'src_python/myldpc/helpers',
        ],
        language='c++',
        extra_compile_args=compile_args,
    ),
]

setup(
    name='myldpc',
    version='0.1',
    packages=['myldpc', 'myldpc.bp_decoder', 'myldpc.helpers'],
    package_dir={'': 'src_python'},
    ext_modules=cythonize(ext_modules, language_level=3, include_path=['src_python']),
    install_requires=['numpy', 'scipy', 'cython'],
    zip_safe=False,
) 