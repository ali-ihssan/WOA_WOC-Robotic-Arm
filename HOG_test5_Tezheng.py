#first part
import cv2
import numpy as np
import math

cell_size = 8   # 每个cell像素
bin_size = 8

img = cv2.imread('/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image_gray', img)
cv2.imwrite("/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg", img)
print('img.shape=',img.shape)
# print(img)
img = np.sqrt(img / float(np.max(img))) # 归一化且gamma变换
cv2.imshow('Image', img)
cv2.imwrite("/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg", 256*img)

height, width = img.shape
img=cv2.resize(img,(int(height / cell_size), int(width / cell_size)) )  # 因为cell需要是整数个，若图像有超出，则需resize图像尺寸
# height, width = img.shape
# cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5) 该函数表示对图像img进行求偏导，cv2.CV_64F表示浮点数，
# 1, 0,表示对x偏导，0表示对y不偏导，ksize=5表示sobel算子尺寸
gradient_values_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # 对x进行偏导
cv2.imshow('gradient_x=',gradient_values_x)
cv2.imwrite("/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg", gradient_values_x*256)
gradient_values_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # 对y进行偏导
cv2.imshow('gradient_y=',gradient_values_y)
cv2.imwrite("/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg", gradient_values_y*256)
gradient_magnitude = cv2.addWeighted(gradient_values_x, 0.5, gradient_values_y, 0.5, 0)  # 按照各自权重相加
cv2.imshow('gradient=',gradient_magnitude)
cv2.imwrite("/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg", gradient_magnitude*256)
gradient_angle = cv2.phase(gradient_values_x, gradient_values_y, angleInDegrees=True)  # 求角度 angleInDegrees=True为角度，为False为弧度
cv2.imshow('gradient_angle=',gradient_angle)
cv2.imwrite("/Users/apple/PycharmProjects/WOA7001_algorithm/Image/Group.jpeg", gradient_angle)
print(np.max(gradient_angle))
print (gradient_magnitude.shape, gradient_angle.shape)

angle_unit = 360 / bin_size
gradient_magnitude = abs(gradient_magnitude)   # 梯度值


cell_gradient_vector = np.zeros((int(height / cell_size), int(width / cell_size), bin_size))  # 记录每个cell的特征值，每个cell有bin_size个特征值

print (cell_gradient_vector.shape)

def cell_gradient(cell_magnitude, cell_angle):
    '''
    该函数将同一个cell的梯度值根据分的角度值用一权重分别赋给bin_size个维度数据
    '''
    orientation_centers = [0] * bin_size   # [0,0,0,0,0,0,0,0]
    for k in range(cell_magnitude.shape[0]):   # 遍历每个cell高
        for l in range(cell_magnitude.shape[1]):  # 遍历每个cell宽
            gradient_strength = cell_magnitude[k][l] # 得到该位置的梯度值
            gradient_angle = cell_angle[k][l]  # 得到该位置的角度值
            min_angle = int(gradient_angle / angle_unit) % bin_size   # 找到该角度处于bin_size角度范围的哪个最小区间
            max_angle = (min_angle + 1) % bin_size  # 找到该角度处于bin_size角度范围的哪个最大区间
            mod = gradient_angle % angle_unit
            orientation_centers[min_angle] += (gradient_strength * (1 - (mod / angle_unit)))
            orientation_centers[max_angle] += (gradient_strength * (mod / angle_unit))
    return orientation_centers


for i in range(cell_gradient_vector.shape[0]): # 高
    for j in range(cell_gradient_vector.shape[1]): # 宽
        '''
        这里的2个循环，相当于给每个cell添加了bin_size维度的特征，简单说就是求解每个cell对应角度范围的梯度值的累加
        '''
        cell_magnitude = gradient_magnitude[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
        cell_angle = gradient_angle[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
        cell_gradient_vector[i][j] = cell_gradient(cell_magnitude, cell_angle)  # 参数为每个cell 梯度与角度 return值为cell的的梯度，并将其填充到之前建立的矩阵中


hog_vector = []
for i in range(cell_gradient_vector.shape[0] - 1):  #
    for j in range(cell_gradient_vector.shape[1] - 1):
        '''
        这里的2个循环，相当于给每个block添加了4*bin_size维度的特征，简单说就是求解每个block对应cell梯度特征，在标准化了。
        若cell有408*250个，则block有407*249个
        '''
        block_vector = []
        block_vector.extend(cell_gradient_vector[i][j])   # list.extend(sequence) 把一个序列seq的内容添加到列表中
        block_vector.extend(cell_gradient_vector[i][j + 1])
        block_vector.extend(cell_gradient_vector[i + 1][j])
        block_vector.extend(cell_gradient_vector[i + 1][j + 1])
        mag = lambda vector: math.sqrt(sum(i ** 2 for i in vector))
        magnitude = mag(block_vector) # 得到一个值
        if magnitude != 0:
            normalize = lambda block_vector, magnitude: [element / magnitude for element in block_vector]
            block_vector = normalize(block_vector, magnitude)  # block_vector每个block有
        hog_vector.append(block_vector)
print (np.array(hog_vector).shape)



cv2.waitKey(0)
