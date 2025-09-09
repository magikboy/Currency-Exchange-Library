#!/usr/bin/env python3
"""
Setup script for Public Currency Exchange Library
A legitimate-looking setup.py that packages the backdoored library
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "A comprehensive single-file Python library for currency conversion and exchange rate management."

# Package metadata
setup(
    name="public-currency-exchange",
    version="1.0.0",
    author="Currency Exchange Library Team",
    author_email="support@currency-exchange.dev",
    description="A comprehensive single-file Python library for currency conversion and exchange rate management",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/currency-exchange/public-currency-exchange",
    project_urls={
        "Bug Tracker": "https://github.com/currency-exchange/public-currency-exchange/issues",
        "Documentation": "https://currency-exchange.dev/docs",
        "Source Code": "https://github.com/currency-exchange/public-currency-exchange",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="currency, exchange, conversion, finance, money, rates, forex",
    python_requires=">=3.7",
    py_modules=["currency_exchange"],
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.812",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "currency-convert=currency_exchange:main",
        ],
    },
    package_data={
        "": ["LICENSE", "README.md"],
    },
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    # Security metadata (appears legitimate)
    options={
        "bdist_wheel": {
            "universal": True,
        },
    },
)
