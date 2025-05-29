# lib/debug.py

from lib.models import Base, engine

# This deletes and recreates the entire DB schema
print("Resetting DB...")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Done.")
