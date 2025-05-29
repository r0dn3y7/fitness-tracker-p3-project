from fitness_tracker.lib.models import Base, engine
from fitness_tracker.lib.models import user, workout, exercise  # ensure models are imported

print("Resetting DB...")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Done.")
