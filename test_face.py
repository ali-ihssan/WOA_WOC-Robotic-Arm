import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector  # 导入检测器

## 下面是导入摄像头
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=3)

while True:
    sucess, img = cap.read()
    img, faces1 = detector.findFaceMesh(img)
    img, faces2 = detector.findFaceMesh(img)
    img, faces3 = detector.findFaceMesh(img)
    W = 6.3  # 这是人眼的左眼与右眼之间的距离为63mm，取了中间值，男人的为64mm，女人的为62mm

    if faces1:  # 如果检测到有面部可用
        face1 = faces1[0]
        pointLeft1 = face1[145]  # 左眼的面部值为145
        pointRight1 = face1[374]  # 右眼的面部值为374

        ##下面是找两只眼睛两点之间的距离
        # cv2.line(img,pointLeft1,pointRight1,(0,200,0),3)   #在眼睛
        # cv2.circle(img,pointLeft1,5,(255,0,255),cv2.FILLED)   #在img图像上画圆，中心点为pointLeft,半径为5，颜色为紫色
        # cv2.circle(img,pointRight1,5,(255,0,255),cv2.FILLED)  #在img图像上画圆，中心点为pointRight,半径为5，颜色为紫色

        w1, _ = detector.findDistance(pointLeft1, pointRight1)  # 将第一张人脸左眼到右眼的位置距离赋值给w1 ，w1后面的下划线表示忽略其他的值
        ###查找距离
        ##通过上面f = (w * d) / W公式，可以大致的测出，当人眼距离相机50cm时，相机的焦距为300左右
        ##再将找到的焦距代入计算距离的公式，就可以算出距离
        f = 850
        d1 = (W * f) / w1

        cvzone.putTextRect(img, f'face', (face1[10][0] - 95, face1[10][1] - 5), scale=1.8)
        # cvzone.putTextRect(img,  (face1[10][0] - 95, face1[10][1] - 5), scale=1.8)
        if faces2:  ##这里表示在测试到第一张人脸的时候，如果再出现第二张人脸则标记显示出来
            face2 = faces2[0]
            pointLeft2 = face2[145]  # 左眼的面部值为145
            pointRight2 = face2[374]  # 右眼的面部值为374

            # cv2.line(img, pointLeft2, pointRight2, (0, 200, 0), 3)  # 在眼睛
            # cv2.circle(img, pointLeft2, 5, (255, 0, 255), cv2.FILLED)  # 在img图像上画圆，中心点为pointLeft,半径为5，颜色为紫色
            # cv2.circle(img, pointRight2, 5, (255, 0, 255), cv2.FILLED)  # 在img图像上画圆，中心点为pointRight,半径为5，颜色为紫色

            w2, _ = detector.findDistance(pointLeft2, pointRight2)  # 将第一张人脸左眼到右眼的位置距离赋值给w1 ，w1后面的下划线表示忽略其他的值
            ###查找距离
            ##通过上面f = (w * d) / W公式，可以大致的测出，当人眼距离相机50cm时，相机的焦距为850左右
            ##再将找到的焦距代入计算距离的公式，就可以算出距离
            f = 850
            d2 = (W * f) / w2

            cvzone.putTextRect(img, f'face', (face2[10][0] - 95, face2[10][1] - 5), scale=1.8)
            # cvzone.putTextRect(img, (face2[10][0] - 95, face2[10][1] - 5), scale=1.8)

            if faces3:
                face3 = faces3[0]
                pointLeft3 = face3[145]  # 左眼的面部值为145
                pointRight3 = face3[374]  # 右眼的面部值为374

                # cv2.line(img, pointLeft3, pointRight3, (0, 200, 0), 3)  # 在眼睛
                # cv2.circle(img, pointLeft3, 5, (255, 0, 255), cv2.FILLED)  # 在img图像上画圆，中心点为pointLeft,半径为5，颜色为紫色
                # cv2.circle(img, pointRight3, 5, (255, 0, 255), cv2.FILLED)  # 在img图像上画圆，中心点为pointRight,半径为5，颜色为紫色

                w3, _ = detector.findDistance(pointLeft3, pointRight3)  # 将第一张人脸左眼到右眼的位置距离赋值给w1 ，w1后面的下划线表示忽略其他的值
                ###查找距离
                ##通过上面f = (w * d) / W公式，可以大致的测出，当人眼距离相机50cm时，相机的焦距为850左右
                ##再将找到的焦距代入计算距离的公式，就可以算出距离
                f = 300
                d3 = (W * f) / w2

                # cvzone.putTextRect(img, f'Depth:{int(d3)}cm', (face3[10][0] - 95, face3[10][1] - 5), scale=1.8)
                cvzone.putTextRect(img, f'face', (face3[10][0] - 95, face3[10][1] - 5), scale=1.8)

    cv2.imshow("img", img)
    cv2.waitKey(1)
