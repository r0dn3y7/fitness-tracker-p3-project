from lib.models import Base, engine

print("Resetting DB...")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Done.")
