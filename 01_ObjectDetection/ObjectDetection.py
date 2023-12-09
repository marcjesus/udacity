import cv2

# Read the image
image = cv2.imread('images/faces.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
face_classifier = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

# Detect faces using the grayscale image
faces = face_classifier.detectMultiScale(gray, 1.0485258, 6)

# When no faces detected, face_classifier returns an empty array
if len(faces) == 0:
    print("No faces found")
else:
    # Iterate through faces and draw rectangles over each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (127, 0, 255), 2)
        cv2.imshow('Face Detection', image)
        cv2.waitKey(0)

cv2.destroyAllWindows()
