from setuptools import setup

setup(name='titan',
      version='2.0',
      description='elecTric fIeld generaTion And maNipulation',
      author='Thijs Stuyver',
      author_email='thijsstuyver@hotmail.com',
      license='GPLv3',
      packages=['titan'],
      include_package_data=True,
      package_data={'':['*.json']},
      zip_safe=False)
