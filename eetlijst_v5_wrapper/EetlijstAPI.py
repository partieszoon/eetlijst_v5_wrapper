import re
import requests
import json
import datetime
from graphql_utils import load_graphql_queries
from os import environ

DEFAULT_BASE_URL = "https://api.samenn.nl/v1/graphql"

class EetlijstAPI:
    base_url = DEFAULT_BASE_URL
    headers = None
    queries = None
    
    def __init__(self, bearer_token: str, base_url: str = DEFAULT_BASE_URL):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json'
        }
        self.queries = load_graphql_queries()
    
    def getEetschemaToday(self) -> dict:
        """Get the eetschema for today.
        """
        today = datetime.date.today().isoformat()
        return self.getEetschemaOnDate(today)
    
    def getCooksAndAttendeesToday(self) -> dict:
        """Get the cooks and attendees for today.
        """
        today = datetime.date.today().isoformat()
        return self.getCooksAndAttendeesOnDate(today)
    
    def getCooksAndAttendeesOnDate(self, date: str) -> dict:
        """Get the cooks and attendees for a specific date.

        Args:
            date (str): The date in ISO format (YYYY-MM-DD).

        Returns:
            dict: A dictionary containing the response from the API.
        """
        return self.execute_query("GetCooksAndAttendeesOnDate", self.queries["GetCooksAndAttendeesOnDate"], {"date": date})
    
    def getEetschemaOnDate(self, date: str) -> dict:
        """Get the full eetschema for a specific date.

        Args:
            date (str): The date in ISO format (YYYY-MM-DD).

        Returns:
            dict: A dictionary containing the response from the API.
        """
        return self.execute_query("GetEetschemaOnDate", self.queries["GetEetschemaOnDate"], {"date": date})

    def getBasicGroupInfo(self) -> dict:
        """Get basic information about a group.
        """
        return self.execute_query("GetBasicGroupInfo", self.queries["GetBasicGroupInfo"])

    def getLaatstGekookt(self) -> dict:
        """Get the last time each user cooked.
        """
        res = self.execute_query("GetLaatstGekookt", self.queries["GetLaatstGekookt"])
        res.sort(key=lambda x: x["order"])
        return res

    def execute_query(self, operation: str, query: str, variables: dict = None, raw = False) -> dict:
        """
        Executes a GraphQL query on the API.

        Args:
            query (str): The GraphQL query string.
            variables (dict, optional): Variables for the query, if any.
            raw (bool, optional): If True, return the raw response from the API. Defaults to False.

        Returns:
            dict: The JSON response from the API.
        """
        # GraphQL payload
        payload = {
            "operationName": operation,
            "query": query,
            "variables": variables or {}
        }
        try:
            response = requests.post(self.base_url, headers=self.headers, json=payload)
            response.raise_for_status()
            res = response.json()
            if raw:
                return res
            if res.get("errors"):
                raise APIError(res["errors"])
            if len(res) == 1: # if there is only one key in the response, return the value of that key
                return res["data"][list(res["data"].keys())[0]]
            return res["data"]
        except requests.exceptions.RequestException as e:
            raise APIError(e) # catch, wrap and re-raise the exception. Corporate Programming™ at its finest.

class APIError(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)

# Example usage:
if __name__ == "__main__":
    # Your GraphQL API endpoint and Bearer token
    bearer_token = environ.get("EETLIJST_BEARER_TOKEN") or input("Bearer token: ")

    # Initialize GraphQL API client
    api_client = EetlijstAPI(bearer_token)

    responses = [
        api_client.getEetschemaToday(),
        api_client.getCooksAndAttendeesToday(),
        api_client.getBasicGroupInfo(),
        api_client.getLaatstGekookt()
    ]

    for response in responses:
        if response:
            print(json.dumps(response, indent=2))
