import os


class PathManager:
    def __init__(self) -> None:
        pass

    def get_source_dir():
        return "/Game"

    def get_file_log_path() -> str:
        return os.path.dirname(__file__) + "//PythonLog.txt"

    def get_mesh_destination_folder():
        return '/Game/Meshes'

    def get_sound_destination_folder():
        return '/Game/Sounds'

    def get_texture_destination_folder():
        return '/Game/Textures'