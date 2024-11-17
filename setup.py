from setuptools import setup, find_packages

setup(
    name="eetlijst_v5_wrapper",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",  # Include any external dependencies you have
    ],
    package_data={
        'my_graphql_package': [
            'resources/queries/*.graphql',  # Include all .graphql files in the package
            'resources/schema.graphql',
        ],
    },
    include_package_data=True,
    description="A simple package for interacting with the Eetlijst GraphQL API",
    author="Joeri"
)
