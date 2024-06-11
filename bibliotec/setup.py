from setuptools import setup

setup (
    name='biblioteca',
    version='1.0',
    description='Conjunto de funciones para manipular una biblioteca de libros',
    author='Carlos Scarpini',
    author_email='carlosscarpinibr@gmail.com',
    url='www.retinaclinic.com.br',
    packages=['biblioteca', 'biblioteca.buscarautor', 'biblioteca.eliminarlibro', 'biblioteca.entrarlibro', 'biblioteca.mostrarlibros', 'biblioteca.verificarbiblioteca'],
    scripts=[]
    )