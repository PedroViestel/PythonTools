from infrastructure.configuration.path_manager import PathManager
from infrastructure.data.base_repository import BaseRepository

class EditorRepository(BaseRepository):
    def list(self, workingPath: str = PathManager.get_source_dir()):
        allAssets = self.editorAssetLibrary.list_assets(workingPath, True, False)
        return allAssets