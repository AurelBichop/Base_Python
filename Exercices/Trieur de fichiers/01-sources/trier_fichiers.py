import os
import glob
import shutil

ext_fichiers = {
    "MUSIQUE": ["mp3", "wav"],
    "VIDEOS": ["mp4", "mov"],
    "IMAGES": ["jpeg", "jpg"],
    "DOCUMENTS": ["pdf"],
}

path_to_target = r"d:/FORMATION_Language_DEV/PYTHON_3/Exercices/Trieur de fichiers/01-sources/tri_fichiers_sources/"

for folder in ext_fichiers:
    os.makedirs(
        r"d:/FORMATION_Language_DEV/PYTHON_3/Exercices/Trieur de fichiers/01-sources/"+folder, 777, True)
    for ext_file in ext_fichiers[folder]:
        path_to_file_list = glob.glob(path_to_target + '*'+ext_file)
        for path_to_file in path_to_file_list:
            shutil.move(
                path_to_file, r"d:/FORMATION_Language_DEV/PYTHON_3/Exercices/Trieur de fichiers/01-sources/"+folder)
