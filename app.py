import streamlit as st
import cv2
import numpy as np
from PIL import Image

# -------------------------------
# App Title
# -------------------------------
st.title("👁️ Face and Eye Detection using OpenCV")
st.write("Upload an image to detect **faces and eyes** using Haar Cascades.")

# -------------------------------
# Load Haar Cascade Classifiers
# -------------------------------
face_classifier = cv2.CascadeClassifier(
    "/Users/sasidharbhagavatula/Desktop/python/haarcascade/haarcascade_frontalface_default.xml"
)

eye_classifier = cv2.CascadeClassifier(
    "/Users/sasidharbhagavatula/Desktop/python/haarcascade/haarcascade_eye.xml"
)
st.write("Face cascade loaded:", not face_classifier.empty())
st.write("Eye cascade loaded:", not eye_classifier.empty())

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Convert uploaded file to OpenCV image
    image = Image.open(uploaded_file).convert("RGB")
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        st.warning("⚠️ No face detected")

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (127, 0, 255), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_classifier.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(
                roi_color,
                (ex, ey),
                (ex + ew, ey + eh),
                (255, 255, 0),
                2
            )

    # Convert back to RGB for Streamlit
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display result
    st.image(img, caption="Detected Face(s) and Eye(s)", use_container_width=True)