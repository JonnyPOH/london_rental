from pipelines.training_pipeline import training_pipeline


if __name__ == "__main__":
    # Run the pipeline
    training_pipeline(data_path="/home/jonnyoh/code/JonnyPOH/recommend/data/olist_customers_dataset.csv")
    print("Pipeline run successfully!")
