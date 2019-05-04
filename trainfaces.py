import cv2
import os
import imutils
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import time

def extract_embeddings(directory):
    detector = cv2.dnn.readNetFromCaffe(
        'face_detection_model/deploy.prototxt',
        'face_detection_model/res10_300x300_ssd_iter_140000.caffemodel'
    )

    embedder = cv2.dnn.readNetFromTorch('openface_nn4.small2.v1.t7')

    image_paths = []
    for root, dirs, files in os.walk(directory):
        image_paths = image_paths + [os.path.join(root, f) for f in files if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

    total = 0
    known_embeddings = []
    known_names = []

    for i, image_path in enumerate(image_paths):
        print("Processing ", image_path)
        image = cv2.imread(image_path)
        image = imutils.resize(image, width=600)
        (h, w) = image.shape[:2]
        head, _ = os.path.split(image_path)
        head, name = os.path.split(head)
        image_blob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)), 1.0, (300, 300),
            (104.0, 177.0, 123.0), swapRB=False, crop=False)
        
        detector.setInput(image_blob)
        detections = detector.forward()

        if len(detections) > 0:
            i = np.argmax(detections[0, 0, :, 2])
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                # extract the face ROI and grab the ROI dimensions
                face = image[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                # ensure the face width and height are sufficiently large
                if fW < 20 or fH < 20:
                    continue

                # construct a blob for the face ROI, then pass the blob
                # through our face embedding model to obtain the 128-d
                # quantification of the face
                faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                    (96, 96), (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput(faceBlob)
                vec = embedder.forward()

                # add the name of the person + corresponding face
                # embedding to their respective lists
                known_names.append(name)
                known_embeddings.append(vec.flatten())
                total += 1

    data = {"embeddings": known_embeddings, "names": known_names}
    f = open("embeddings.pkl", "wb")
    f.write(pickle.dumps(data))
    f.close()

def train_model():
    data = pickle.loads(open('embeddings.pkl', "rb").read())
    le = LabelEncoder()
    labels = le.fit_transform(data["names"])
    recognizer = SVC()

    recognizer = SVC(C=1.0, kernel="linear", probability=True)
    recognizer.fit(data["embeddings"], labels)

    f = open('recognizer.pkl', "wb")
    f.write(pickle.dumps(recognizer))
    f.close()

    # write the label encoder to disk
    f = open('le.pkl', "wb")
    f.write(pickle.dumps(le))
    f.close()

def recognize_faces(img_path):
    start_time = time.time()
    detector = cv2.dnn.readNetFromCaffe(
        'face_detection_model/deploy.prototxt',
        'face_detection_model/res10_300x300_ssd_iter_140000.caffemodel'
    )
    embedder = cv2.dnn.readNetFromTorch('openface_nn4.small2.v1.t7')
    recognizer = pickle.loads(open('recognizer.pkl', "rb").read())
    le = pickle.loads(open('le.pkl', "rb").read())

    image = cv2.imread(img_path)
    image = imutils.resize(image, width=600)
    (h, w) = image.shape[:2]

    # construct a blob from the image
    imageBlob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 1.0, (300, 300),
        (104.0, 177.0, 123.0), swapRB=False, crop=False)

    # apply OpenCV's deep learning-based face detector to localize
    # faces in the input image
    detector.setInput(imageBlob)
    detections = detector.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections
        if confidence > 0.75:
            # compute the (x, y)-coordinates of the bounding box for the
            # face
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # extract the face ROI
            face = image[startY:endY, startX:endX]
            (fH, fW) = face.shape[:2]

            # ensure the face width and height are sufficiently large
            if fW < 20 or fH < 20:
                continue

            # construct a blob for the face ROI, then pass the blob
            # through our face embedding model to obtain the 128-d
            # quantification of the face
            faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
                (0, 0, 0), swapRB=True, crop=False)
            embedder.setInput(faceBlob)
            vec = embedder.forward()

            # perform classification to recognize the face
            preds = recognizer.predict_proba(vec)[0]
            j = np.argmax(preds)
            proba = preds[j]
            name = le.classes_[j]
            end_time = time.time()
            return j, proba

            # draw the bounding box of the face along with the associated
            # probability
            #text = "{}: {:.2f}%".format(name, proba * 100)
            #y = startY - 10 if startY - 10 > 10 else startY + 10
            #cv2.rectangle(image, (startX, startY), (endX, endY),
            #    (0, 0, 255), 2)
            #cv2.putText(image, text, (startX, y),
            #    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
    return None
    # show the output image
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

#def setup_data():

#extract_embeddings('data')
#train_model()

#print(recognize_faces('57210745_424343178361531_7059295302397722624_n.jpg'))