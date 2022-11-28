from application.shared.result import Result
from domain.entity.asset_data import MaterialAssetData
from unreal import SystemLibrary, EditorAssetLibrary, BlendMode

class MaterialService():
    def __init__(self, _editorAssetLibrary: EditorAssetLibrary, _systemLibrary: SystemLibrary):
        self.editorAssetLibrary = _editorAssetLibrary
        self.systemLibrary = _systemLibrary

    def is_material_missing_phys_mat(self, asset) -> Result:
        materialData = MaterialAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if materialData.is_material_or_material_instance() and not self.systemLibrary.is_valid(materialData.phys_material):
            result.message = ("        %s ------------> At Path: %s \n" % (materialData.assetName, materialData.assetPathName))

        return result

    def is_materials_using_translucency(self, asset) -> Result:
        materialData = MaterialAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if materialData.is_material() and materialData.get_blend_mode() == BlendMode.BLEND_TRANSLUCENT:
            result.message = ("        %s ------------> At Path: %s \n" % (materialData.assetName, materialData.assetPathName))

        return result

    def is_two_sided_material(self, asset) -> Result:
        materialData = MaterialAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if materialData.is_material() and materialData.is_two_sided():
            result.message = ("        %s ------------> At Path: %s \n" % (materialData.assetName, materialData.assetPathName))

        return result