from setuptools import setup, find_packages

setup(
    name='json_patch',
    author='Chris Ermel',
    author_email='ermel272@gmail.com',
    version='0.0.0',
    description='An implementation of IETF RFC 6902',
    license='MIT',
    url='github.com/ermel272/json-patch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='JSON pointer IETF RFC 6902',
    install_requires=[
        # json_pointer TODO: uncomment once json_pointer is published on the PYPI
    ],
    extras_require={
        'dev': [
            'setuptools==36.2.7',
            'sphinx==1.6.3'
        ],
        'test': [
            'nose==1.3.7',
            'coverage==4.4.1',
            'coveralls==1.2.0'
        ]
    },
    packages=find_packages(),
    include_package_data=True
)
