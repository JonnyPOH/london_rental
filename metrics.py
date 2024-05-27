from zenml.client import Client

artifact = Client().get_artifact_version('e4b4690d-073d-43dc-a77b-64b264426215')
loaded_artifact = artifact.load()
