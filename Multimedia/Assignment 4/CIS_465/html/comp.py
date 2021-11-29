import cv2
import enhance
import equalizer

if __name__ == "__main__":

    # both these image look ok. The AINDANE looks a more artistic, while the AHE exposes more detail. The AHE also has
    # more artifacts

    Original = cv2.imread("images/low-light.jpg")
    print("Please be patient, this could take a while... A long while")
    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    equal = equalizer.equalize_color(Original)
    print("Equalize")
    print(equal)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # The AINDANE looks bad, cetain color are over represented. Don't do the orginal image justice. The AHE looks good.
    # good color and detail

    Original = cv2.imread("images/image.bmp")
    print("Please be patient, this could take a while")
    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    equal = equalizer.equalize_color(Original)
    print("Equalize")
    print(equal)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # These both look good. The both inhance some of the datail in different ways. TH AHE looks to be closer to the 
    # original color

    Original = cv2.imread("images/cat.jpg")
    print("Please be patient, this could take a while")
    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    equal = equalizer.equalize_color(Original)
    print("Equalize")
    print(equal)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # The both appear quite diffeent from the original. The AHE looks to expose more detail, expecially in the sky.
    # I also like the artitic styling better

    Original = cv2.imread("images/dark-sky.jpg")
    print("Please be patient, this could take a while")
    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    equal = equalizer.equalize_color(Original)
    print("Equalize")
    print(equal)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # These both have some large artificts, but the AHE looks pretty close to the original, considering the original is very dark
    # AINDANE Looks tarible, with completely off color artifacts

    Original = cv2.imread("images/dark.jpg")
    print("Please be patient, this could take a while")
    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    equal = equalizer.equalize_color(Original)
    print("Equalize")
    print(equal)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Once again AHE looks better. However, AINDANE has truer to life coloring, while AHE results in some significan
    # color changes

    Original = cv2.imread("images/bright.jpg")
    print("Please be patient, this could take a while")
    Enhanced = enhance.enhance(Original)
    print("Enhanced")
    print(Enhanced)
    cv2.imshow("Enhanced", Enhanced)

    equal = equalizer.equalize_color(Original)
    print("Equalize")
    print(equal)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()