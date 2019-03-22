from setuptools import setup
from setuptools import find_packages

setup(name='backoffice',
      version='0.0.1',
      url='https://github.com/JeonWookTae/feature_backoffice',
      license='MIT',
      author='wook',
      author_email='wooktae@gmail.com',
      python_requires='>=3.6',
      packages=find_packages(exclude=['example', '__pycache__']),
      zip_safe=False,
      install_requires=[
            'xlrd==1.1.0'
      ],
      classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3'
      ])