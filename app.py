from flask import Flask, render, templater, request, redirect, url_for

app = Flask(__name__)

class task:
    def __init__(self, title):
        self.title = title
