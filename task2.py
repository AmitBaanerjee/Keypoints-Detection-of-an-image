import cv2
import numpy as np
import math

image=cv2.imread('task2.jpg',0)

b,h=image.shape
    
def gaussian_function(x,y,sigma):
    part1=(-((x**2 + y**2)/(2*sigma**2)))
    part2=(1/(2*(3.14)*(sigma**2)))
    return part2* math.exp(part1)

def gaussian_kernel(sigma):
    output=[]
    sum=0
    for i in range(0,7):
        row=[]
        for j in range(0,7):
            val=gaussian_function(j-3,3-i,sigma)
            sum=sum + val
            row.append(val)
        output.append(row) 
    x=np.asarray(output)/sum
    return x    

def blurring(kernel,image):
    b,h=image.shape
    empimg = np.asarray([[0.0 for col in range(h)] for row in range(b)])
    for i in range(3, b-3):
        for j in range(3, h-3):  
            gx = (kernel[0][0] * image[i-3][j-3]) + (kernel[0][1] * image[i-3][j-2]) + \
             (kernel[0][2] * image[i-3][j-1]) + (kernel[0][3] * image[i-3][j]) + \
             (kernel[0][4] * image[i-3][j+1]) + (kernel[0][5] * image[i-3][j+2]) + \
             (kernel[0][6] * image[i-3][j+3]) + (kernel[1][0] * image[i-3][j-3]) + \
             (kernel[1][1] * image[i-3][j-2]) + \
             (kernel[1][2] * image[i-3][j-1]) + (kernel[1][3] * image[i-3][j]) + \
             (kernel[1][4] * image[i-3][j+1]) + (kernel[1][5] * image[i-3][j+2]) + \
             (kernel[1][6] * image[i-3][j+3]) + \
             (kernel[2][0] * image[i-3][j-3]) + \
             (kernel[2][1] * image[i-3][j-2]) + \
             (kernel[2][2] * image[i-3][j-1]) + (kernel[2][3] * image[i-3][j]) + \
             (kernel[2][4] * image[i-3][j+1]) + (kernel[2][5] * image[i-3][j+2]) + \
             (kernel[2][6] * image[i-3][j+3]) +\
             (kernel[3][0] * image[i-3][j-3]) + \
             (kernel[3][1] * image[i-3][j-2]) + \
             (kernel[3][2] * image[i-3][j-1]) + (kernel[3][3] * image[i-3][j]) + \
             (kernel[3][4] * image[i-3][j+1]) + (kernel[3][5] * image[i-3][j+2]) + \
             (kernel[3][6] * image[i-3][j+3]) + \
             (kernel[4][0] * image[i-3][j-3]) + \
             (kernel[4][1] * image[i-3][j-2]) + \
             (kernel[4][2] * image[i-3][j-1]) + (kernel[4][3] * image[i-3][j]) + \
             (kernel[4][4] * image[i-3][j+1]) + (kernel[4][5] * image[i-3][j+2]) + \
             (kernel[4][6] * image[i-3][j+3]) + \
             (kernel[5][0] * image[i-3][j-3]) + \
             (kernel[5][1] * image[i-3][j-2]) + \
             (kernel[5][2] * image[i-3][j-1]) + (kernel[5][3] * image[i-3][j]) + \
             (kernel[5][4] * image[i-3][j+1]) + (kernel[5][5] * image[i-3][j+2]) + \
             (kernel[5][6] * image[i-3][j+3]) + \
             (kernel[6][0] * image[i-3][j-3]) + \
             (kernel[6][1] * image[i-3][j-2]) + \
             (kernel[6][2] * image[i-3][j-1]) + (kernel[6][3] * image[i-3][j]) + \
             (kernel[6][4] * image[i-3][j+1]) + (kernel[6][5] * image[i-3][j+2]) + \
             (kernel[6][6] * image[i-3][j+3])
            empimg[i-3][j-3] = gx
    return empimg

#scaling logic for octave2 
def scaling(image,octavenum):
    b,h=image.shape
    image2=[]    
    for i in range(0,b-1,2):
        row1=[]
        for j in range(0,h-1,2):
            val=image[i][j]
            row1.append(val)
        image2.append(row1)
    image2=np.asarray(image2)
    cv2.imwrite("scaledoct%simg.png" %octavenum,image2)
    return image2

#generating all images for a single octave
def img_generator(octavesigma,image,octavenumber):
    for i in range(5):
        sig=octavesigma[i]
        ker=gaussian_kernel(sig)
        empimg=blurring(ker,image)
        cv2.imwrite('blurimgoct%s_%s.png' %(octavenumber,i) ,empimg)

#Function for octave 1 blurred images
def o1():
    oct1sig=[0.70,1,1.414,2,2.82]
    img_generator(oct1sig,image,1)
     
#Function for octave 2 blurred images 
def o2():
    oct2sig=[1.41,2,2.82,4,5.65]
    oct2img=scaling(image,2)
    img_generator(oct2sig,oct2img,2)
    return oct2img
#Function for octave 3 blurred images
def o3():
    oct3sig=[2.82,4,5.65,8,11.31]
    oct3img=scaling(o2(),3)
    img_generator(oct3sig,oct3img,3)
    return oct3img
#Function for octave 4 blurred images
def o4():
    oct4sig=[5.65,8,11.31,16,22.62]
    oct4img=scaling(o3(),4)
    img_generator(oct4sig,oct4img,4)

o1()
o2()
o3()
o4()
#Reading first octave images
oct10=cv2.imread('blurimgoct1_0.png',0)
oct11=cv2.imread('blurimgoct1_1.png',0)
oct12=cv2.imread('blurimgoct1_2.png',0)
oct13=cv2.imread('blurimgoct1_3.png',0)
oct14=cv2.imread('blurimgoct1_4.png',0)

#calculating DOG for Octave 1
dog10=oct11-oct10
dog11=oct12-oct11
dog12=oct13-oct12
dog13=oct14-oct13 

#Reading second octave images
oct20=cv2.imread('blurimgoct2_0.png',0)
oct21=cv2.imread('blurimgoct2_1.png',0)
oct22=cv2.imread('blurimgoct2_2.png',0)
oct23=cv2.imread('blurimgoct2_3.png',0)
oct24=cv2.imread('blurimgoct2_4.png',0)

#calculating DOG for Octave 2
dog20=oct21-oct20
cv2.imwrite('dog20.png',dog20)
dog21=oct22-oct21
cv2.imwrite('dog21.png',dog21)
dog22=oct23-oct22
cv2.imwrite('dog22.png',dog22)
dog23=oct24-oct23
cv2.imwrite('dog23.png',dog23)

#Reading third octave images
oct30=cv2.imread('blurimgoct3_0.png',0)
oct31=cv2.imread('blurimgoct3_1.png',0)
oct32=cv2.imread('blurimgoct3_2.png',0)
oct33=cv2.imread('blurimgoct3_3.png',0)
oct34=cv2.imread('blurimgoct3_4.png',0)

#calculating DOG for Octave 3
dog30=oct31-oct30
cv2.imwrite('dog30.png',dog30)
dog31=oct32-oct31
cv2.imwrite('dog31.png',dog31)
dog32=oct33-oct32
cv2.imwrite('dog32.png',dog32)
dog33=oct34-oct33
cv2.imwrite('dog33.png',dog33)

#Reading fourth octave images
oct40=cv2.imread('blurimgoct4_0.png',0)
oct41=cv2.imread('blurimgoct4_1.png',0)
oct42=cv2.imread('blurimgoct4_2.png',0)
oct43=cv2.imread('blurimgoct4_3.png',0)
oct44=cv2.imread('blurimgoct4_4.png',0)

#calculating DOG for Octave 4
dog40=oct41-oct40
dog41=oct42-oct41
dog42=oct43-oct42
dog43=oct44-oct43

#finding maxima and minima points.
imagecolor=cv2.imread('task2.jpg')

#keypoint detection
def generatepoints(prevdog,currentdog,nextdog,scale):
    w,d=currentdog.shape
    for i in range(1,w-1):
        for j in range(1,d-1):
            target=currentdog[i,j]
            compare=[]
            for k in range(-1,2):
                for l in range(-1,2):
                    compare.append(prevdog[i+k][j+l])
                    compare.append(nextdog[i+k][j+l])
            for p in range(-1,2):
                for q in range(-1,2):
                    if(i==i+p and j==j+q):
                        continue
                    else:
                        compare.append(currentdog[i+k][j+l])
            compare.sort()
            if(compare[0] > target or compare[len(compare)-1]< target):
                rowval=i*scale
                colval=j*scale
                imagecolor[rowval,colval]=255

generatepoints(dog10,dog11,dog12,1)
generatepoints(dog11,dog12,dog13,1)
generatepoints(dog20,dog21,dog22,2)
generatepoints(dog21,dog22,dog23,2)
generatepoints(dog30,dog31,dog32,4)
generatepoints(dog31,dog32,dog33,4)
generatepoints(dog40,dog41,dog42,8)
generatepoints(dog41,dog42,dog43,8)
#displaying the final output image
cv2.imwrite('keydetectedimage.png',imagecolor)

