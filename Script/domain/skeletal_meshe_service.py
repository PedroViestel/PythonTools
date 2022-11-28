from application.shared.result import Result
from domain.entity.asset_data import SkeletalMeshAssetData
from unreal import EditorAssetLibrary, EditorSkeletalMeshLibrary, SystemLibrary, SkeletalMesh

class SkeletalMeshService():
    def __init__(self, _editorAssetLibrary: EditorAssetLibrary, _editorSkeletalMeshLibrary: EditorSkeletalMeshLibrary, _systemLibrary: SystemLibrary):
        self.editorAssetLibrary = _editorAssetLibrary
        self.editorSkeletalMeshLibrary = _editorSkeletalMeshLibrary
        self.systemLibrary = _systemLibrary

    def mesh_has_no_lods(self, asset) -> Result:
        skeletonMesheData = SkeletalMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if skeletonMesheData.is_skeleton_mesh():
            _skeletonMeshAsset = SkeletalMesh.cast(skeletonMesheData.asset)
            lod_count = self.editorSkeletalMeshLibrary.get_lod_count(_skeletonMeshAsset)

            if lod_count <= 1:
                result.message = ("        %s ------------> At Path: %s \n" % (skeletonMesheData.assetName, skeletonMesheData.assetPathName))

        return result

    def mesh_num_of_materials(self, asset, numOfMatsToCheckFor) -> Result:
        skeletonMesheData = SkeletalMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if skeletonMesheData.is_skeleton_mesh():
            _skeletonMeshAsset = SkeletalMesh.cast(skeletonMesheData.asset)
            _howManyMaterials = len(_skeletonMeshAsset.get_editor_property("materials"))

            if _howManyMaterials >= numOfMatsToCheckFor:
                result.message = ("        %s ------------> At Path: %s \n" % (skeletonMesheData.assetName, skeletonMesheData.assetPathName))

        return result

    def mesh_has_no_physics_asset(self, asset) -> Result:
        skeletonMesheData = SkeletalMeshAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if skeletonMesheData.is_skeleton_mesh():
            _skeletonMeshAsset = SkeletalMesh.cast(skeletonMesheData.asset)
            _physicsAsset = SkeletalMesh.cast(_skeletonMeshAsset).physics_asset

            if not self.systemLibrary.is_valid(_physicsAsset):
                result.message = ("        %s ------------> At Path: %s \n" % (skeletonMesheData.assetName, skeletonMesheData.assetPathName))

        return result