#!/usr/bin/python3
"""Defines the State class and Base object."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state table."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
