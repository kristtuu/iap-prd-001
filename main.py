from pathlib import Path

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

base_dir = Path(__file__).resolve().parent

def addition(img1, img2, properties):
    augstums, platums, kanali = properties
    result = np.zeros((augstums, platums, kanali), dtype=np.uint8)
    for i in range(augstums):
        for j in range(platums):
            for k in range(kanali):
                a = img1[i, j, k] / 255
                b = img2[i, j, k] / 255
                c = a + b

                if c > 1:
                    result[i, j, k] = 255
                else:
                    result[i, j, k] = np.uint8(round(c * 255))

    Image.fromarray(result).save(base_dir / 'result_addition.png', 'PNG')

def lighten(img1, img2, properties):
    augstums, platums, kanali = properties
    result = np.zeros((augstums, platums, kanali), dtype=np.uint8)
    for i in range(augstums):
        for j in range(platums):
            for k in range(kanali):
                a = img1[i, j, k]
                b = img2[i, j, k]

                if a > b:
                    result[i, j, k] = a
                else:
                    result[i, j, k] = b
    Image.fromarray(result).save(base_dir / 'result_lighten.png', 'PNG')

def dodge(img1, img2, properties):
    augstums, platums, kanali = properties
    result = np.zeros((augstums, platums, kanali), dtype=np.uint8)
    for i in range(augstums):
        for j in range(platums):
            for k in range(kanali):
                a = img1[i, j, k] / 255
                b = img2[i, j, k] / 255

                if a == 1:
                    result[i, j, k] = 255
                else:
                    c = (b) / (1 - a)
                    if c > 1:
                        result[i, j, k] = 255
                    else:
                        result[i, j, k] = np.uint8(round(c * 255))

    Image.fromarray(result).save(base_dir / 'result_dodge.png', 'PNG')

def soft_light(img1, img2, properties):
    augstums, platums, kanali = properties
    result = np.zeros((augstums, platums, kanali), dtype=np.uint8)
    for i in range(augstums):
        for j in range(platums):
            for k in range(kanali):
                a = img1[i, j, k] / 255
                b = img2[i, j, k] / 255

                if a <= 0.5:
                    c = (2 * a - 1) * (b - b**2) + b
                else:
                    c = (2 * a - 1) * (b**(1/2) - b) + b

                result[i, j, k] = np.uint8(round(c * 255))

    Image.fromarray(result).save(base_dir / 'result_soft_light.png', 'PNG')

def main():
    img1 = np.array(Image.open(base_dir / 'img-one.png').convert('RGB'))
    img2 = np.array(Image.open(base_dir / 'img-two.png').convert('RGB'))
    properties = img1.shape

    if img1.shape[0] != img2.shape[0] or img1.shape[1] != img2.shape[1]:
        print('[!] Attēliem jābūt vienāda izmēra')
        return
    
    addition(img1, img2, properties)
    lighten(img1, img2, properties)
    dodge(img1, img2, properties)
    soft_light(img1, img2, properties)

if __name__ == "__main__":
    main()
