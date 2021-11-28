import os
import shutil

from main import TEMP_FOLDER_DIRECTORY, PROGRAM_ROOT_PATH, CHART_IMAGES_DIRECTORY, DAILY_VALUES_INPUT_FILES_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def removeTemporaryFiles():
    temp_directory = os.path.join(PROGRAM_ROOT_PATH, TEMP_FOLDER_DIRECTORY)
    for filename in os.listdir(temp_directory):
        file_path = os.path.join(temp_directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def createRequiredDirectoriesIfDoesNotExists():
    for directory_to_create in [CHART_IMAGES_DIRECTORY, DAILY_VALUES_INPUT_FILES_DIRECTORY, YEARLY_VALUES_INPUT_FILES_DIRECTORY]:
        path_for_directory = os.path.join(PROGRAM_ROOT_PATH, TEMP_FOLDER_DIRECTORY, directory_to_create)
        if not os.path.exists(path_for_directory):
            os.makedirs(path_for_directory)
