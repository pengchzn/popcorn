import setuptools

with open('README.md', 'r') as fp:
    long_description = fp.read()

setuptools.setup(
    name='yonder',
    version='1.0',
    description='A pYthON package for Data dEnoising and Reconstruction',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/pengchzn/yonder',
    keywords=['Astrostatistics techniques', 'Astronomy software', 'Astronomy data analysis'],
    author='Rafael S. de Souza, Peng Chen',
    author_email='drsouza@shao.ac.cn, pengchzn@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python :: 3',
    ],
)
