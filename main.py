
import os
import zipfile
from program.logics.utils import paths

try:
     
    import tkinter as tk
    
except ImportError:
    print("Ce programme a besoin que le module 'tkinter' soit installé")
    exit()

from program.gui.window import Window


def extract_res():
    assets_file = zipfile.ZipFile(file=paths.res_filepath)
    assets_file.extractall(path=paths.assets_dir)

if __name__ == "__main__":

    if not os.path.exists(paths.assets_dir):
        os.mkdir(paths.assets_dir)

    if not os.path.exists(paths.end_game_dir):

        try:
            extract_res()

        except Exception as e:
            print(f"Error : {e}")

    if not os.path.exists(paths.pendu_images_dir):
                
        try:
            extract_res()

        except Exception as e:
            print(f"Error : {e}")

    app = Window()
    app.switch_menu_fr()
    app.mainloop()
