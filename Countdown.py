import os
import zipfile

""" Global constants """
data_zip = "data.zip"               # The zip archive
clean_files = [".csv", ".jpg"]      # File extensions to clean


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


def main():
    unzip_data()
    clean_data()

if __name__ == "__main__":
    main()
