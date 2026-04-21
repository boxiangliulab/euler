from setuptools import setup, find_packages

setup(
    name='euler',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'networkx',
        'numpy',
        'rich',
        'scipy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'euler=euler.main:main',
            'euler-somatic=euler.analysis.euler_somatic:main',
        ],
    },
    author='Laurentiusia',
    author_email='e1124923@u.nus.edu',
    description='euler - cEll-resolved Umi-Linked haplotypE Reconstruction',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/boxiangliulab/Faser-scRNA',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
