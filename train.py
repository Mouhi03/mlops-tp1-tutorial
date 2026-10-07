import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


def execute_pipeline():

    print("[MLOps Pipeline] Starting pipeline execution...")

    # ==========================================
    # 1. Load the Iris dataset
    # ==========================================
    raw_data = load_iris(as_frame=True)

    # Convert the dataset into a Pandas DataFrame
    df = raw_data.frame

    # ==========================================
    # 2. Separate features (X) and target (y)
    # ==========================================
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # ==========================================
    # 3. Split the dataset
    # ==========================================
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # ==========================================
    # 4. Create the Random Forest model
    # ==========================================
    classifier = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # ==========================================
    # 5. Train the model
    # ==========================================
    classifier.fit(X_train, y_train)

    # ==========================================
    # 6. Create the models directory
    # ==========================================
    os.makedirs("models", exist_ok=True)

    # ==========================================
    # 7. Save the trained model
    # ==========================================
    with open("models/iris_model.pkl", "wb") as f:
        pickle.dump(classifier, f)

    # ==========================================
    # 8. Evaluate the model
    # ==========================================
    score = classifier.score(X_test, y_test)

    print(
        f"[MLOps Pipeline] Target model successfully cached! "
        f"Score: {score:.4f}"
    )


# ==============================================
# Execute the pipeline
# ==============================================
if __name__ == "__main__":
    execute_pipeline()