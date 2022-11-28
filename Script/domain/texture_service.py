import math
from application.shared.result import Result
from domain.entity.asset_data import Texture2DAssetData
from infrastructure.utils.unreal_extensions import UnrealEditorAssetLibrary

class TextureService():
    def __init__(self, _editorAssetLibrary: UnrealEditorAssetLibrary):
        self.editorAssetLibrary = _editorAssetLibrary

    def number_is_power_of_2(self, n):
        return (math.log(n) / math.log(2)).is_integer()

    def validate_power_of_two_texture(self, asset) -> Result:
        texture2D = Texture2DAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if texture2D.is_texture_2D():
            if not self.number_is_power_of_2(texture2D.textureYsize) or not self.number_is_power_of_2(texture2D.textureXsize):
                result.message = ("        [%s x %s] %s ------------> At Path: %s \n" % (texture2D.textureXsize, texture2D.textureYsize, texture2D.assetName, texture2D.assetPathName))

        return result

    def validate_texture_x_size(self, asset, sizeOfTexToCheckAgainst) -> Result:
        texture2D = Texture2DAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if texture2D.is_texture_2D():
            if texture2D.textureYsize == sizeOfTexToCheckAgainst and texture2D.textureXsize == sizeOfTexToCheckAgainst:
                result.message = "        [%sx%s] %s ------------> At Path: %s \n" % (texture2D.textureXsize, texture2D.textureYsize, texture2D.assetName, texture2D.assetPathName)

        return result