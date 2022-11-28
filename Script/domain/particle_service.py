from application.shared.result import Result
from domain.entity.asset_data import ParticleAssetData
from unreal import EditorAssetLibrary

class ParticleService():
    def __init__(self, _editorAssetLibrary: EditorAssetLibrary):
        self.editorAssetLibrary = _editorAssetLibrary

    def particles_has_no_lods(self, asset) -> Result:
        particleData = ParticleAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if particleData.is_particle_system() and particleData.lod_count <= 1:
            result.message = ("        %s ------------> At Path: %s \n" % (particleData.assetName, particleData.assetPathName))

        return result