
from distutils.core import setup

setup(
    name='abstract',
    keywords='NLP,Chinese,Keywords extraction, Abstract extraction',
    install_requires=['jieba >= 0.35', 'numpy >= 1.7.1', 'networkx >= 1.9.1'],
    packages=['abstract'],
    package_dir={'abstract':'abstract'},
    package_data={'abstract':['*.txt',]},
)