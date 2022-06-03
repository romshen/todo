#! /usr/bin/env bash

python3 -c '''from api.models import Base
from api.database import engine

Base.metadata.create_all(bind=engine)
'''
