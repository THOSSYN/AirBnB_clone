#!/usr/bin/python3
""" The special init file """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
