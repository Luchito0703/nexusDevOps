from setuptools import setup, find_packages
setup(
    name='milib-ejemplo',
    version='0.0.1',
    author='Tu Nombre',
    author_email="ejemplo@email.com",
    description='Una librería de ejemplo para subir cosas a Nexus',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)