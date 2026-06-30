from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, precision_score
from sklearn.metrics import recall_score, f1_score


# Loading Iris dataset
flower_data = load_iris()

# Features and labels
flower_features = flower_data.data
flower_labels = flower_data.target

print("Dataset loaded successfully.")
print("Flower classes:", flower_data.target_names)
print("-" * 40)


# Splitting dataset into training and testing portions
train_x, test_x, train_y, test_y = train_test_split(
    flower_features,
    flower_labels,
    test_size=0.20,
    shuffle=True,
    random_state=42
)

print("Training samples:", len(train_x))
print("Testing samples :", len(test_x))
print("-" * 40)


# Scaling helps KNN perform better
scaler = StandardScaler()

scaled_train_x = scaler.fit_transform(train_x)
scaled_test_x = scaler.transform(test_x)


# Creating KNN classifier
flower_classifier = KNeighborsClassifier(n_neighbors=5)

# Learning patterns from training data
flower_classifier.fit(scaled_train_x, train_y)

# Predicting unseen samples
predicted_output = flower_classifier.predict(scaled_test_x)


# Evaluating model performance
acc = accuracy_score(test_y, predicted_output)
pre = precision_score(test_y, predicted_output, average="weighted")
rec = recall_score(test_y, predicted_output, average="weighted")
f1 = f1_score(test_y, predicted_output, average="weighted")

print("Model Results")
print("-" * 40)
print("Accuracy :", round(acc, 4))
print("Precision:", round(pre, 4))
print("Recall   :", round(rec, 4))
print("F1 Score :", round(f1, 4))
print()


# Confusion matrix
print("Confusion Matrix")
print(confusion_matrix(test_y, predicted_output))
print()


#print statements
print("Classification Report")
print(
    classification_report(
        test_y,
        predicted_output,
        target_names=flower_data.target_names
    )
)