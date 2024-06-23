from setuptools import setup, find_packages
from os import path

setup(
    name='sf2_loader',
    packages=find_packages(),
    version='1.25',
    license='LGPLv2.1',
    description=
    'This is an easy-to-use soundfonts loader, player and audio renderer in python',
    author='Rainbow-Dreamer',
    author_email='1036889495@qq.com',
    url='https://github.com/Rainbow-Dreamer/sf2_loader',
    download_url=
    'https://github.com/Rainbow-Dreamer/sf2_loader/archive/1.25.tar.gz',
    keywords=['soundfont', 'sf2', 'python'],
    install_requires=['pydub', 'musicpy', 'numpy', 'py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    include_package_data=True)
