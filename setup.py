from setuptools import setup, find_packages
setup(
    name='milib-ejemplo',
    version='0.0.5',
    author='Luis',
    author_email="luchito@email.com",
    description='Una librería de ejemplo para subir cosas a Nexus',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)