from setuptools import setup, find_packages

setup(
    name="test_package_alex_mcp",
    version="0.1.0",
    description="A short description of your package",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "setuptools"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "test-mcp-command=test_mcp.__main__:main"
        ]
    }
)
