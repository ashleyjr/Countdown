import os
import zipfile
import cv2

""" Global constants """
data_zip = "data.zip"               # The zip archive
clean_files = [".csv", ".jpg"]      # File extensions to clean
data_file = "data.csv"
img_ext = ".jpg"


def unzip_data():
    """ Unzip the data held in zip file """
    zip_ref = zipfile.ZipFile(data_zip, 'r')
    zip_ref.extractall('')
    zip_ref.close()


def clean_data():
    """ Clean up all the unzipped data """
    for clean_file in clean_files:
        file_list = [f for f in os.listdir(".") if f.endswith(clean_file)]
        for f in file_list:
            os.remove(f)


def downscale_image(img, bottom, x, y):
    """
        Take bottom section of image
        Rescale
        Threshold around mean of image
    """
    #ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
    #img = cv2.Canny(img,100,200)
    width, height = tuple(img.shape[1::-1])
    img = img[int(round((1 - bottom) * (height - 1))):(height - 1), 1:(width - 1)]
    img = cv2.resize(img, (x, y))
    img = cv2.Canny(img, 100, 200)
    #ret, img = cv2.threshold(img, img.mean(), 255, cv2.THRESH_BINARY)
    return img


def main():
    unzip_data()
    file_list = [f for f in os.listdir(".") if f.endswith(img_ext)]
    for file in file_list:
        cv2.imwrite(file, downscale_image(cv2.imread(file, 0), 0.2, 60, 20))
    clean_data()

if __name__ == "__main__":
    main()
