
import os
import __main__

res_filepath = os.path.join(os.path.dirname(os.path.dirname(__main__.__file__)), "assets.zip")
windows_localdata_dir = os.path.join(os.getenv("LOCALAPPDATA", os.path.join(os.path.expanduser("~"), "AppData", "Local")), "Pendu8")
assets_dir = os.path.join(windows_localdata_dir, "assets")
pendu_images_dir = os.path.join(assets_dir, "pendu")
end_game_dir = os.path.join(assets_dir, "end_game")
