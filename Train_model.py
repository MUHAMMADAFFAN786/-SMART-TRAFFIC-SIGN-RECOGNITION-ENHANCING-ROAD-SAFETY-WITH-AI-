import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2
import pathlib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import warnings
warnings.filterwarnings("ignore")


# 1. Dataset path

data_dir = r"E:\MY CODE\TRAFFIC_SIGN_RECO\GTSRB"
train_csv = pd.read_csv(os.path.join(data_dir, "train.csv"))


# 2. Load images and labels

X, y = [], []
for i, row in train_csv.iterrows():
    img_path = os.path.join(data_dir, row['Path'])
    image = cv2.imread(img_path)
    image = cv2.resize(image, (32, 32))
    X.append(image)
    y.append(row['ClassId'])

X = np.array(X) / 255.0   # Normalize
y = to_categorical(y, num_classes=43)


# 3. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


# 4. Data Augmentation

datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.15,
    width_shift_range=0.1,
    height_shift_range=0.1
)

# 5. Show some sample images

train_path = os.path.join(data_dir, "Train")
img_dir = pathlib.Path(train_path)
NUM_CATEGORIES = 43
IMG_WIDTH, IMG_HEIGHT = 32, 32

plt.figure(figsize=(14, 14))
for i in range(NUM_CATEGORIES):
    plt.subplot(7, 7, i + 1)
    sign = list(img_dir.glob(f'{i}/*'))[0]
    img = load_img(sign, target_size=(IMG_WIDTH, IMG_HEIGHT))
    plt.imshow(img)
plt.pause(3)
plt.close()

# 6. Build CNN model

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D(2, 2),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(43, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


# 7. Train Model

history = model.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    validation_data=(X_test, y_test),
    epochs=15
)

# 8. Evaluate

loss, acc = model.evaluate(X_test, y_test)
print(f" Test Accuracy: {acc*100:.2f}%")


# 9. Accuracy & Loss Graphs

plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.legend()
plt.title('Model Accuracy')

plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.legend()
plt.title('Model Loss')
plt.show()


# 10. Test predictions on sample images

def predict_sample_images():
    fig, axes = plt.subplots(3, 5, figsize=(12, 8))
    for i, ax in enumerate(axes.flat):
        img = X_test[i]
        true_label = np.argmax(y_test[i])
        pred_label = np.argmax(model.predict(img.reshape(1, 32, 32, 3), verbose=0))
        ax.imshow(img)
        ax.set_title(f"Pred: {pred_label} | True: {true_label}")
        ax.axis('off')
    plt.show()

predict_sample_images()


# 11. Save Model (always save at the end)

save_path = os.path.join(data_dir, "traffic_sign_model.h5")
model.save(save_path)
print(f"Model saved successfully at: {save_path}")











