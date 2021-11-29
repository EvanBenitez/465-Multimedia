import cv2
import enhance

if __name__ == "__main__":

    # the enhanced image looks much brighter and more vibrant. IT does have some obvious artifacts in the windows though
    
    Original = cv2.imread("images/image.bmp")
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # A tiny bit of artifacting, the image looks brighter, but the orignal was already bright so it seems over exposed

    Original = cv2.imread("images/bright.jpg")
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # this looks slightly brighter, didn't really need it. there is some minor artifacting

    Original = cv2.imread("images/cat.jpg")
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # looks like the hill was suddenly populated by cherry blossoms. THe picture is brighter, but the red kind of
    # ruins it

    Original = cv2.imread("images/dark-sky.jpg")
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Sky looks pretty good, the rest, not so great. Seems to work best with some dark images, as long as they are not too dark

    Original = cv2.imread("images/dark.jpg")
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Looks pretty similar to the orignal, doesn't seem to have flush out any more detail.
    # the original feel of the image I think is lost

    Original = cv2.imread("images/low-light.jpg")
    print("Original")
    print(Original)
    cv2.imshow("Original", Original)

    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    cv2.waitKey(0)
    cv2.destroyAllWindows()