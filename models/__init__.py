#!/usr/bin/python3
"""this file makes the directory called models a package"""
from models.engine.file_storage.py import FileStorage


storage = FileStorage()
storage.reload()
