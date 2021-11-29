import cv2
import numpy
import sys

# Black and white image
def I(image):
    red, green, blue = cv2.split(image)
    #grey_image = numpy.zeros(len(image), len(image[0]))

    gray_image = 76.245/255 * red + 149.685/255 * green + 29.071/255 * blue
    return gray_image.astype(numpy.uint8)

# takes a gray image and returns it in normal form
def I_normal(image):
    return image/255

# Luminance Enhancement
def I_normal_prime(image):
    normal = I_normal(image)
    prime = numpy.zeros( (len(image),len(image[0])) )
    z = Z(image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            part1 = pow(normal[i][j], 0.75 * z + 0.25)
            part2 = (1 - normal[i][j]) * 0.4 * (1 - z)
            part3 = pow(normal[i][j], 2-z)
            prime[i][j] = (part1 + part2 + part3) / 2
    return prime
    
def Z(image):
    levels = {}
    for row in image:
        for col in row:
            levels[col] = levels.get(col, 0) + 1
    histo = sorted(levels.items())
    # get cummulitive distribution up to 10%
    ten_percent = round(numpy.size(image) / 10)
    cd = (0,0)
    prev = histo[0][0]
    for tup in histo:
        cd = (tup[0], cd[1] + tup[1])
        if cd[1] >= ten_percent:
            if cd[1] - ten_percent > ten_percent - cd[1] + tup[1]:
                cd = (prev, cd[1] - tup[1])
            break
        prev = tup[0]
    # get z
    if cd[0] <= 50:
        return 0
    elif cd[0] > 150:
        return 1
    else:
        return (cd[0] - 50) / 100

# Gauss blur image
def Iconv(image):
    return cv2.GaussianBlur(image, (0,0), 60)

def P(image):
    # Standard Deviation
    mean = numpy.sum(image) / numpy.size(image)
    sum = 0
    for row in image:
        for col in row:
            sum += pow(col - mean, 2)
    sd = pow(sum/numpy.size(image), .5)

    # get P
    if sd <= 3:
        return 3
    elif sd >= 10:
        return 1
    else:
        return (27 - 2 * sd) / 7

def E(image):
    r = numpy.zeros( (len(image), len(image[0])) )
    convoluted = Iconv(image)
    p = (image)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == 0:
                 r[i][j] = 1
            else:
                r[i][j] = convoluted[i][j] / image[i][j]
    return numpy.power(r, P(image))

# contrast inhancement
def S(image):
    Iprime = I_normal_prime(image)
    e = E(image)
    S = numpy.zeros( (len(image), len(image[1])) )
    for i in range(len(image)):
        for j in range(len(image[i])):
            S[i][j] = 255 * pow(Iprime[i][j], e[i][j])
    return S.astype(numpy.uint8)

# restore color to the enhanced image
def color_restore(color, gray, contrast):
    lambda_r = 1
    lambda_g = 1
    lambda_b = 1
    output = numpy.zeros( (len(color), len(color[0]), 3) )
    red, green, blue = cv2.split(color)

    for i in range(len(output)):
        for j in range(len(output[i])):
            output[i][j][0] = contrast[i][j] * (red[i][j] / (gray[i][j] + 1e-6)) * lambda_r
            output[i][j][1] = contrast[i][j] * (green[i][j] / (gray[i][j] + 1e-6)) * lambda_g
            output[i][j][2] = contrast[i][j] * (blue[i][j] / (gray[i][j] + 1e-6)) * lambda_b
    return numpy.clip(output, 0, 255).astype(numpy.uint8)

def enhance(image):
    gray = I(image)
    contrast = S(gray)
    return color_restore(image,gray,contrast)


def max_out(number):
    if number > 255:
        #print(number)
        return 255
    return number

if __name__ == "__main__":
    Original = cv2.imread(sys.argv[1])
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

   
    

    #test code not implemented in final version
    # img = cv2.imread("images/image.bmp")
    # cv2.imshow("Original color", img)
    # gray_image = I(img)
    # cv2.imshow("gray",gray_image)
    # print(gray_image)

    # gray_image_normal = I_normal(gray_image)
    # cv2.imshow("gray normal",gray_image_normal)
    # print(gray_image_normal)

    # luminance_image = I_normal_prime(gray_image)
    # cv2.imshow("luminance",luminance_image)
    # print(luminance_image)

    # gauss_image = Iconv(gray_image)
    # cv2.imshow("gauss",gauss_image)
    # print(gauss_image)
    
    # Contrast = S(gray_image)
    # print(Contrast)
    # cv2.imshow("Contrast Enhancement", Contrast)
   
    # Restored = color_restore(img, gray_image, Contrast)
    # print(Restored)
    # cv2.imshow("Color Restoration", Restored)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    