# HTTP Requests with Python Requests Library
import requests
import json
from time import sleep

def basic_requests():
    """Demonstrate basic HTTP requests"""
    # GET request
    print("GET request example:")
    response = requests.get('https://api.github.com/users/github')
    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Content Type: {response.headers['content-type']}")
    
    # Parse JSON response
    data = response.json()
    print(f"\nGitHub User Info:")
    print(f"Name: {data.get('name')}")
    print(f"Location: {data.get('location')}")
    print(f"Followers: {data.get('followers')}")

def http_methods():
    """Demonstrate different HTTP methods"""
    # POST request
    print("\nPOST request example:")
    post_data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=post_data
    )
    print(f"POST Response: {response.json()}")
    
    # PUT request
    print("\nPUT request example:")
    put_data = {'id': 1, 'title': 'updated foo', 'body': 'updated bar', 'userId': 1}
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/1',
        json=put_data
    )
    print(f"PUT Response: {response.json()}")
    
    # DELETE request
    print("\nDELETE request example:")
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    print(f"DELETE Status Code: {response.status_code}")

def request_parameters():
    """Demonstrate request parameters and headers"""
    # Query parameters
    params = {
        'q': 'python',
        'sort': 'stars',
        'order': 'desc'
    }
    
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Python Requests Example'
    }
    
    response = requests.get(
        'https://api.github.com/search/repositories',
        params=params,
        headers=headers
    )
    
    data = response.json()
    print("\nGitHub Search Results:")
    for repo in data.get('items', [])[:3]:
        print(f"Repository: {repo['name']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"URL: {repo['html_url']}\n")

def error_handling():
    """Demonstrate error handling with requests"""
    try:
        # Intentionally invalid URL
        response = requests.get('https://api.github.com/invalid')
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"\nHTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def session_example():
    """Demonstrate using sessions"""
    with requests.Session() as session:
        # Set default headers for all requests in this session
        session.headers.update({
            'User-Agent': 'Python Requests Session Example',
            'Accept': 'application/json'
        })
        
        # Make multiple requests using the same session
        print("\nSession requests:")
        for user in ['github', 'torvalds', 'gvanrossum']:
            response = session.get(f'https://api.github.com/users/{user}')
            if response.ok:
                data = response.json()
                print(f"User: {data.get('name')} - Followers: {data.get('followers')}")
            sleep(1)  # Be nice to the API

if __name__ == "__main__":
    basic_requests()
    http_methods()
    request_parameters()
    error_handling()
    session_example() 