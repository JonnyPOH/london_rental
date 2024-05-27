from pipelines.training_pipeline import training_pipeline
from zenml.client import Client

if __name__ == "__main__":
    # Run the pipeline
    print(f" URI: Client().active_stack.experiment_tracker.get_tracking_uri()")
    training_pipeline(data_path="/home/jonnyoh/code/JonnyPOH/recommend/data/olist_customers_dataset.csv")
    print("Pipeline run successfully!")
