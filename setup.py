from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="facilitation-lang",
    version="1.0.0",
    author="Pedro",
    author_email="seu-email@exemplo.com",
    description="Uma linguagem de programação em português para facilitar o aprendizado",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perepepeu/facilitation-lang",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Software Development :: Interpreters",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "facilitation=facilitation.cli:main",
        ],
    },
    keywords="programming language, education, portuguese, interpreter",
    project_urls={
        "Bug Reports": "https://github.com/perepepeu/facilitation-lang/issues",
        "Source": "https://github.com/perepepeu/facilitation-lang",
        "Documentation": "https://github.com/perepepeu/facilitation-lang#readme",
    },
    include_package_data=True,
    package_data={
        "facilitation": ["*.f"],
    },
) 