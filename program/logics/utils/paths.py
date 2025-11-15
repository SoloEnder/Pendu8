
import os
import __main__
iscompiled = False
main_filepath = __main__.__file__
base_dir = os.path.dirname(os.path.dirname(main_filepath)) if iscompiled else os.path.dirname(main_filepath)
res_filepath = os.path.join(base_dir, "assets.zip")
# windows_localdata_dir = os.path.join(os.getenv("LOCALAPPDATA", os.path.join(os.path.expanduser("~"), "AppData", "Local")), "Pendu8")
assets_dir = os.path.join(base_dir, "assets")
pendu_images_dir = os.path.join(assets_dir, "pendu")
end_game_dir = os.path.join(assets_dir, "end_game")
