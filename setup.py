from setuptools import setup
import textwrap

setup(name='MarkupPy',
      version='1.12',
      description='An HTML/XML generator',
      url='http://markup.sf.net/',
      author='Daniel Nogradi',
      author_email="nogradi@gmail.com",
      long_description=textwrap.dedent("""\
        This is markup.py - a Python module that attempts to make it easier to generate HTML/XML from a Python program in an intuitive, lightweight, customizable and pythonic way. It works with both python 2 and 3.
    
        The code is in the public domain.

        Version: 1.12 as of July 12 2017.

        Please send bug reports, feature requests, enhancement ideas or questions to nogradi at gmail dot com.
 
        Installation: Run 'pip install MarkupPy" from the terminal.
    
        Documentation and further info is at http://markup.sourceforge.net/
        
        (Migrated from markup.py)
        """),
      license="MIT",
      packages=['MarkupPy'],
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      zip_safe=False)
