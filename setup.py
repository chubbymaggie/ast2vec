from importlib.machinery import SourceFileLoader
from setuptools import setup, find_packages
import sys

sourcedml = SourceFileLoader("sourced.ml", "./sourced/ml/__init__.py").load_module()

with open("README.md") as f:
    long_description = f.read()

if sys.version_info < (3, 5, 0):
    typing = ["typing"]
else:
    typing = []

setup(
    name="sourced-ml",
    description="Framework for machine learning on source code. "
                "Provides API and tools to train and use models based "
                "on source code features extracted from Babelfish's UASTs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=".".join(map(str, sourcedml.__version__)),
    license="Apache 2.0",
    author="source{d}",
    author_email="machine-learning@sourced.tech",
    url="https://github.com/src-d/ml",
    download_url="https://github.com/src-d/ml",
    packages=find_packages(exclude=("sourced.ml.tests",)),
    namespace_packages=["sourced"],
    entry_points={
        "console_scripts": ["srcml=sourced.ml.__main__:main"],
    },
    keywords=["machine learning on source code", "word2vec", "id2vec",
              "github", "swivel", "bow", "bblfsh", "babelfish"],
    install_requires=["PyStemmer>=1.3,<2.0",
                      "bblfsh>=2.2.1,<3.0",
                      "modelforge>=0.7.0,<0.8",
                      "sourced-engine>=0.7.0,<0.8",
                      "humanize>=0.5.0,<0.6",
                      "parquet>=1.2,<2.0",
                      "pygments>=2.2.0,<3.0",
                      "keras>=2.0,<3.0",
                      "pandas>=0.22,<1.0",
                      "scikit-learn>=0.19,<1.0",
                      "tqdm>=4.20,<5.0"] + typing,
    extras_require={
        "tf": ["tensorflow>=1.0,<2.0"],
        "tf_gpu": ["tensorflow-gpu>=1.0,<2.0"],
    },
    tests_require=["docker>=3.4.0,<4.0"],
    package_data={"": ["LICENSE.md", "README.md"],
                  "sourced": ["ml/transformers/languages.yml"], },
    python_requires=">=3.4",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries"
    ]
)
