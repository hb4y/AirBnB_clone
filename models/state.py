#!/usr/bin/python3
"""
    Implementation of the State class
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
        Implementation for the State.
    """
    name = ""

    def __init__(self, **kargs):
        super().__init__(**kwargs)
