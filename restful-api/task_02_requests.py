#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API.
"""

import csv
import requests


def fetch_and_print_posts():
    """
    Fetch all posts and print status code and titles.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts and save selected data to posts.csv.
    """
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        with open(
            "posts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(
                csv_file,
                fieldnames=["id", "title", "body"]
            )

            writer.writeheader()
            writer.writerows(data)
