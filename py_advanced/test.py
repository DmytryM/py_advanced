# import cv2
#
# face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     success, img = cap.read()
#     #img = cv2.imread("IMG_20191012_145410_3.jpg")
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
#
#     cv2.imshow('rez', img)
#     #cv2.waitKey()
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# ------------------------2

# import torch
# print(torch.cuda.is_available())

# ------------------------3
import keras
import tensorflow
import numpy as np
model = keras.Sequential([tensorflow.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)
print(model.predict([10.0]))
