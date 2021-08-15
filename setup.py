#!/usr/bin/env python3
# Copyright 2019 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup

from precise_lite import __version__

setup(
    name='precise_lite',
    version=__version__,
    license='Apache-2.0',
    author='Matthew Scholefield',
    author_email='matthew.scholefield@mycroft.ai',
    description='Mycroft Precise Wake Word Listener, Lite version (OpenVoiceOS)',
    url='https://github.com/OpenVoiceOS/precise-lite',
    keywords='wakeword keyword wake word listener sound',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=[
        'precise_lite',
        'precise_lite.scripts'
    ],
    entry_points={
        'console_scripts': [
            'precise-lite-add-noise=precise_lite.scripts.add_noise:main',
            'precise-lite-collect=precise_lite.scripts.collect:main',
            'precise-lite-convert=precise_lite.scripts.convert:main',
            'precise-lite-eval=precise_lite.scripts.eval:main',
            'precise-lite-listen=precise_lite.scripts.listen:main',
            'precise-lite-engine=precise_lite.scripts.engine:main',
            'precise-lite-simulate=precise_lite.scripts.simulate:main',
            'precise-lite-test=precise_lite.scripts.test:main',
            'precise-lite-graph=precise_lite.scripts.graph:main',
            'precise-lite-train=precise_lite.scripts.train:main',
            'precise-lite-train-optimize=precise_lite.scripts.train_optimize:main',
            'precise-lite-train-sampled=precise_lite.scripts.train_sampled:main',
            'precise-lite-train-incremental=precise_lite.scripts.train_incremental:main',
            'precise-lite-train-generated=precise_lite.scripts.train_generated:main',
            'precise-lite-calc-threshold=precise_lite.scripts.calc_threshold:main',
        ]
    },
    include_package_data=True,
    install_requires=[
        'numpy',
        'tensorflow==2.3.1',
        'sonopy',
        'pyaudio',
        'h5py',
        'wavio',
        'typing',
        'prettyparse>=1.1.0',
        'precise_lite_runner',
        'attrs',
        'fitipy<1.0',
        'speechpy-fast',
        'pyache'
    ]
)
