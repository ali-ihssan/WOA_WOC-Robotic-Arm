import cv2
import numpy as np
#thres = 0.45 # Threshold to detect object

objectsNames = []
objectsFile = "/Users/apple/PycharmProjects/WOA7001_algorithm/Data_pack/Object_Detection_Files/coco.names"
with open(objectsFile,"rt") as f:
    objectsNames = f.read().rstrip("\n").split("\n")

configPath = "/Users/apple/PycharmProjects/WOA7001_algorithm/Data_pack/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/Users/apple/PycharmProjects/WOA7001_algorithm/Data_pack/Object_Detection_Files/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def HOG_algorithm_identifies_objects_and_distances(frame, confThres, nmsThres, draw=True, objects=[]):

    objectsIds, confs, bbox = net.detect(frame,confThreshold=confThres,nmsThreshold=nmsThres)

    bbox = np.array(bbox)
    x1, y1, x2, y2 = bbox[0]
    actualWidth = 20
    widthInImage = x2 - x1
    focalLength = 1400

    distance = (actualWidth * focalLength) / widthInImage

    if len(objects) == 0: objects = objectsNames
    objectInformation =[]
    if len(objectsIds) != 0:
        for objectsId, confidence,box in zip(objectsIds.flatten(),confs.flatten(),bbox):
            objectName = objectsNames[objectsId - 1]
            if objectName in objects:
                objectInformation.append([box,objectName])
                if (draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,objectsNames[objectsId-1].upper(),(box[0]+10,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.putText(img, "Distance: {:.2f}".format(distance), (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    return img,objectInformation


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    cap.set(3,1000)
    cap.set(4,1000)
    #cap.set(10,70)

    while True:
        success, img = cap.read()
        result, objectInfo = HOG_algorithm_identifies_objects_and_distances(img,0.45,0.2, objects=['toothbrush'])
        #print(objectInfo)
        cv2.imshow("Output",img)
        cv2.waitKey(1)
