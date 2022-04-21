from setuptools import setup
from setuptools import find_namespace_packages as find_packages

setup(
    name="fee-calculator-api",
    version="0.1.0",
    description="Fee calculator for Wolt Summer 2022 Engineering Internships",
    url="https://github.com/mrdimfox/wolt-summer-2022-internships",
    author="Dmitrii Lisin",
    author_email="mrlisdim@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10, <4",
    classifiers=[],
    install_requires=["fastapi", "pydantic"],
    extras_require={
        "dev": [
            "wemake-python-styleguide",
            "mypy",
            "black",
        ],
        "tests": ["pytest", "httpx", "pytest_asyncio"],
    },
    package_data={"fee_calculator_api": ["logger.json"]},
    project_urls={
        "Source": "https://github.com/mrdimfox/wolt-summer-2022-internships",
    },
)
