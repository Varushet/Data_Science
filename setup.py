from setuptools import setup, find_packages

setup(
    name='DATA_SCIENCE',      # Nombre interno
    version='0.1',
    packages=find_packages(), # Encuentra automáticamente 'src' si está bien hecho
    package_dir={'': '.'}     # Busca paquetes desde la raíz
)