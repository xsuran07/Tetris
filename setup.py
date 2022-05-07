from setuptools import setup, find_packages


long_description = (
    'Implemention of the game classical old-school game Tetris.'
    'The realization is based on the pygame framework.'
)


setup(
    name='tetris_sources',
    version='0.1.0',
    author='Jakub Šuráň',
    author_email='xsuran07@stud.fit.vutbr.cz',
    description='Implementation of the Tetris game.',
    long_description=long_description,
    url='https://github.com/xsuran07/Tetris',
    packages=find_packages(),
)
