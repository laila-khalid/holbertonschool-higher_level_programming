import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        
        data = [{'id': post.get('id'),
                 'title': post.get('title'),
                 'body': post.get('body')} for post in posts]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(data)
