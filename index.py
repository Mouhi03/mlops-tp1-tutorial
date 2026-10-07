import pickle
import pandas as pd


# ==========================================
# 1. Load the trained model
# ==========================================
with open("models/iris_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!")
print(model)


# ==========================================
# 2. Create a new sample
# ==========================================
X_new = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=model.feature_names_in_
)


# ==========================================
# 3. Make a prediction
# ==========================================
prediction = model.predict(X_new)

print("Prediction:", prediction)


# ==========================================
# 4. Convert class number to species
# ==========================================
classes = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

print("Species:", classes[prediction[0]])