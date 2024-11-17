import os

DEFAULT_QUERIES_DIRECTORY = os.path.join(os.path.dirname(__file__), "resources", "queries")

def load_graphql_query(file_path):
    """
    Loads a GraphQL query from a .graphql file.

    Args:
        file_path (str): The file path to the GraphQL query file.

    Returns:
        str: The raw GraphQL query string.
    
    Raises:
        FileNotFoundError: If the query file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"GraphQL query file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        query = f.read().strip()

    return query

def load_graphql_queries(directory_path = DEFAULT_QUERIES_DIRECTORY):
    """
    Loads all GraphQL query files from a given directory.

    Args:
        directory_path (str): The directory containing the .graphql files.

    Returns:
        dict: A dictionary where keys are filenames (without extension) and values are the GraphQL queries.
    
    Raises:
        FileNotFoundError: If the directory is not found.
    """
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    queries = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.graphql'):
            query_name = os.path.splitext(filename)[0]
            file_path = os.path.join(directory_path, filename)
            query = load_graphql_query(file_path)
            queries[query_name] = query

    return queries

def load_graphql_schema(file_path):
    """
    Loads a GraphQL schema from a .graphql schema file.

    Args:
        file_path (str): The file path to the GraphQL schema file.

    Returns:
        str: The raw GraphQL schema string.
    
    Raises:
        FileNotFoundError: If the schema file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"GraphQL schema file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        schema = f.read().strip()

    return schema

# Example usage:
if __name__ == "__main__":
    queries_directory = "resources/queries"
    try:
        queries = load_graphql_queries(queries_directory)
        print("Loaded queries:")
        for query_name, query in queries.items():
            print(f"{query_name}: {query[:50]}...")  # Print first 50 characters of each query
    except FileNotFoundError as e:
        print(e)

    # Load schema
    schema_path = "resources/schema.graphql"
    try:
        schema = load_graphql_schema(schema_path)
        print(f"Loaded schema: {schema[:50]}...")  # Print first 50 characters of the schema
    except FileNotFoundError as e:
        print(e)
