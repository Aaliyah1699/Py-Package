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
    url=os.getenv("URL"),  # Homepage of your library (e.g. GitHub or your website)
    keywords=['invoice', 'excel', 'pdf'],
    install_requires=['fpdf', 'openpyxl', "pandas"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Who is the audience for your library?
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',  # Python versions that your library supports
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)