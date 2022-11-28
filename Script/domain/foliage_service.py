from application.shared.result import Result
from domain.entity.asset_data import FoliageAssetData
from unreal import EditorAssetLibrary

class FoliageService():
    def __init__(self, _editorAssetLibrary: EditorAssetLibrary):
        self.editorAssetLibrary = _editorAssetLibrary

    def foliage_has_max_draw_distance(self, asset) -> Result:
        materialData = FoliageAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if materialData.is_foliage() and materialData.maxDrawDistance <= 0:
            result.message = ("        %s ------------> At Path: %s \n" % (materialData.assetName, materialData.assetPathName))

        return result