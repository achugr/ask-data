import requests

url = "https://play.clickhouse.com/?user=explorer"
headers = {
    "Content-Type": "text/plain"
}

def query(query: str) -> str:
    try:
        response = requests.post(url, data=query, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        result = response.text
        print(f"Query is {query}, result is: {result}")
        return result
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err}")  # Re-raise as a general exception
    except Exception as err:
        raise Exception(f"An error occurred: {err}")


