from setuptools import setup
import os
from dotenv import load_dotenv

load_dotenv()

setup(
    name='gen-invoices',
    packages=['invoicing'],
    version='1.0.0',
    license='MIT',
    description='Easily convert Excel invoices into professional PDF formatted invoices, with this Python package, streamlining your invoicing workflow.',
    author=os.getenv("AUTHOR"),
    author_email=os.getenv("EMAIL"),
    url=os.getenv("URL"),  
    keywords=['invoice', 'excel', 'pdf'],
    install_requires=['fpdf', 'openpyxl', "pandas"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',  
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',  # Python versions that gen-invoices library supports
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
