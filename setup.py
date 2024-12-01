from setuptools import setup, find_packages

setup(
    name="eetlijst_v5_wrapper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "requests==2.32.3",
        "urllib3==1.26.16"
    ],
    package_data={
        'eetlijst_v5_wrapper': [
            'resources/queries/*.graphql',  # Include all .graphql files in the package
            'resources/schema.graphql',
        ],
    },
    include_package_data=True,
    description="A simple package for interacting with the Eetlijst GraphQL API",
    author="Joeri"
)
