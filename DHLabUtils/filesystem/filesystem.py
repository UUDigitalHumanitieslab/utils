import zipfile

def unzip(path):
    """
    Unzips a zip folder and creates a folder containing the results
    :param path: The path to the folder to zip
    :return: The new name fo the path
    """
    zip_ref = zipfile.ZipFile(path, 'r')
    new_path = path[:-3]
    zip_ref.extractall(new_path)
    zip_ref.close()
    return new_path