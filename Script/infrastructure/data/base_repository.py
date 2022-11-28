from infrastructure.utils.unreal_extensions import UnrealEditorAssetLibrary


class BaseRepository:
    def __init__(self, _editorAssetLibrary: UnrealEditorAssetLibrary) -> None:
        self.editorAssetLibrary = _editorAssetLibrary

    def list():
        pass