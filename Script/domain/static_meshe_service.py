from application.shared.result import Result
from domain.entity.asset_data import StaticMeshAssetData
from infrastructure.utils.unreal_extensions import UnrealEditorAssetLibrary, UnrealEditorStaticMeshLibrary
import unreal

class StaticMeshService():
    def __init__(self, _editorAssetLibrary: UnrealEditorAssetLibrary, _editorStaticMeshLibrary: UnrealEditorStaticMeshLibrary):
        self.editorAssetLibrary = _editorAssetLibrary
        self.editorStaticMeshLibrary = _editorStaticMeshLibrary

    def mesh_has_no_lods(self, asset) -> Result:
        staticMesheData = StaticMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if staticMesheData.is_static_mesh():
            _staticMeshAsset = unreal.StaticMesh.cast(staticMesheData.asset)
            lod_count = self.editorStaticMeshLibrary.get_lod_count(_staticMeshAsset)

            if lod_count <= 1:
                result.message = ("        %s ------------> At Path: %s \n" % (staticMesheData.assetName, staticMesheData.assetPathName))

        return result

    def mesh_with_no_collision(self, asset) -> Result:
        staticMesheData = StaticMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if staticMesheData.is_static_mesh():
            _staticMeshAsset = unreal.StaticMesh.cast(staticMesheData.asset)
            _TotalNumCollisionElements = self.editorStaticMeshLibrary.get_simple_collision_count(_staticMeshAsset) + self.editorStaticMeshLibrary.get_convex_collision_count(_staticMeshAsset)

            if _TotalNumCollisionElements <= 0:
                result.message = ("        %s ------------> At Path: %s \n" % (staticMesheData.assetName, staticMesheData.assetPathName))

        return result

    def mesh_num_of_materials(self, asset, numOfMatsToCheckFor) -> Result:
        staticMesheData = StaticMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if staticMesheData.is_static_mesh():
            _staticMeshAsset = unreal.StaticMesh.cast(staticMesheData.asset)
            _howManyMaterials = self.editorStaticMeshLibrary.get_number_materials(_staticMeshAsset)

            if _howManyMaterials >= numOfMatsToCheckFor:
                result.message = ("        %s ------------> At Path: %s \n" % (staticMesheData.assetName, staticMesheData.assetPathName))

        return result

    def mesh_has_multiple_uv_channels(self, asset, numOfChannelsToCheckFor) -> Result:
        staticMesheData = StaticMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if staticMesheData.is_static_mesh():
            _staticMeshAsset = unreal.StaticMesh.cast(staticMesheData.asset)
            _howManyUV_channels = self.editorStaticMeshLibrary.get_num_uv_channels(_staticMeshAsset, 0)

            if _howManyUV_channels >= numOfChannelsToCheckFor:
                result.message = ("        %s ------------> At Path: %s \n" % (staticMesheData.assetName, staticMesheData.assetPathName))

        return result