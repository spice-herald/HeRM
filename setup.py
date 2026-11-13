from setuptools import setup, find_packages

setup(
    name='HeRM',
    version='0.2.0',
    packages=find_packages(include=["HeRM", "HeRM.*"]),
    install_requires=[ 'numpy', 'scipy', 'detprocess', 'numba'],
    package_data={
        'HeRM': ['dispersion_curves/*.txt', 'dispersion_curves/*.csv', 'dispersion_curves/*.npy'],
    },
    include_package_data = True
)
