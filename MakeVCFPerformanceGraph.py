import os
import numpy as np
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2
import matplotlib.pyplot as plt

# [LouverAngle, ViewAngle]
VCFs = [[0,90], [0,60], [0,50], [15,90], [25,90]]

degrees = np.arange(-90,91)

BaseImg = cv2.imread("Render/VCFCheck/NoVCF.exr",cv2.IMREAD_UNCHANGED).astype(np.float32)
Bimg_gray = cv2.cvtColor(BaseImg, cv2.COLOR_BGR2GRAY)

for vcf in VCFs:
    illuminance = []
    for i in degrees:
        img = cv2.imread("Render/VCFCheck/LouverAngle_" + str(vcf[0]) + "/ViewAngle_" + str(vcf[1]) + "/" + str(i) + ".exr",cv2.IMREAD_UNCHANGED).astype(np.float32)
        im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        illuminance.append(im_gray.mean())

    plt.plot(degrees,np.asarray(illuminance)/Bimg_gray.mean() * 100, label=str(vcf[0]) + "_" + str(vcf[1]))
plt.legend()
plt.grid()
plt.xticks(np.linspace(-90,90,10))
plt.yticks(np.linspace(0,100,11))
plt.xlim(-60,60)
plt.xlabel("Angle (°)")
plt.ylabel("Total Iluminous Transmittance (%)")
plt.savefig("ResultFigure/CompareWithShinEtsuVCF.png")
