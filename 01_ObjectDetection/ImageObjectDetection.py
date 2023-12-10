import cv2

# Load the pre-trained classifiers for car and person detection
car_classifier = cv2.CascadeClassifier('models/haarcascade_car.xml')
person_classifier = cv2.CascadeClassifier('models/haarcascade_fullbody.xml')

# Read the image
image = cv2.imread('test_video/frame_71.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect cars in the image
cars = car_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Detect persons in the image
persons = person_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected cars
for (x, y, w, h) in cars:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Draw rectangles around the detected persons
for (x, y, w, h) in persons:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the image with detections
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
