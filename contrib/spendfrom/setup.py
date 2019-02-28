from distutils.core import setup
setup(name='BFNspendfrom',
      version='1.0',
      description='Command-line utility for BFN "coin control"',
      author='Gavin Andresen',
      author_email='gavin@BFNfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
