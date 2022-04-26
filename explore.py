import os
import cv2
import json

json_path = "AF_dataset/Amedeo_Modigliani/0.ljson"
with open(json_path) as json_file:
    landmarks = json.load(json_file)

#print(landmarks)

image_path = "AF_dataset/Amedeo_Modigliani/0.png"
image = cv2.imread(image_path)

for point in landmarks['landmarks']['points']:
    x = round(point[1])
    y = round((point[0]))
    image = cv2.circle(image, (x,y), radius=0, color=(255,0,0), thickness=3)


cv2.imshow("TestImage", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

json_path2 = "AF_dataset/Comics/12.ljson"
with open(json_path2) as json_file:
    landmarks2 = json.load(json_file)

print(landmarks2["labels"] == landmarks["labels"])
print(landmarks2["landmarks"]["connectivity"] == landmarks["landmarks"]["connectivity"])
print(landmarks2["landmarks"]["points"] == landmarks["landmarks"]["points"])


