from importlib.machinery import SourceFileLoader
import os

from setuptools import setup, find_packages

model_capacities = ['tiny', 'small', 'medium', 'large', 'full']
weight_files = [
    'model-{}.h5'.format(cap)
    for cap in model_capacities
    if os.path.isfile(os.path.join('crepe', 'model-{}.h5'.format(cap)))
]

version = SourceFileLoader('crepe.version', os.path.join('crepe', 'version.py'))
version = version.load_module()

with open('README.md') as file:
    long_description = file.read()


def read_requirements(filename):
    with open(filename) as requirements_file:
        return [
            line.strip()
            for line in requirements_file
            if line.strip() and not line.lstrip().startswith('#')
        ]


setup(
    name='crepe',
    version=version.version,
    description='CREPE pitch tracker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/marl/crepe',
    author='Jong Wook Kim and Justin Salamon',
    author_email='jongwook@nyu.edu',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['crepe=crepe.cli:main'],
    },
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='tfrecord',
    project_urls={
        'Source': 'https://github.com/marl/crepe',
        'Tracker': 'https://github.com/marl/crepe/issues'
    },
    install_requires=read_requirements(
        os.path.join(os.path.dirname(__file__), "requirements.txt")
    ),
    package_data={
        'crepe': weight_files
    },
)
