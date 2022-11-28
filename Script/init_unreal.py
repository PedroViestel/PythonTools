# from infrastructure.cross_cutting.package_solver import PackageSolver
# PackageSolver.install_missing_packages()
from infrastructure.utils.unreal_extensions import ImportedAssetData
import unreal
from infrastructure.configuration.request import *
from infrastructure.cross_cutting.bootstrapper import Bootstrapper
unreal.log_warning("Init")
mediator = Bootstrapper().get_mediator()

@unreal.uclass()
class PythonExposedClass(unreal.BlueprintFunctionLibrary):
    def __init__(self):
        super().__init__()

    @unreal.ufunction(static=True, params=[bool])
    def log_empty_folders(delete=False):
        with unreal.ScopedEditorTransaction("Delete Empty Folders"):
            mediator.send(LogEmptyFoldersRequest(False))

    @unreal.ufunction(static=True)
    def log_unused_assets():
        mediator.send(LogUnusedAssetsRequest())

    @unreal.ufunction(static=True)
    def log_redirects():
        mediator.send(LogRedirectsRequest())

    @unreal.ufunction(static=True)
    def log_power_of_two_textures():
        mediator.send(LogPowerOfTwoTextures())

    @unreal.ufunction(static=True, params=[int])
    def log_textures_above_x_size(sizeOfTexToCheckAgainst):
        mediator.send(LogTexturesXSize(sizeOfTexToCheckAgainst))

    @unreal.ufunction(static=True)
    def log_materials_missing_phys_mats():
        mediator.send(LogMaterialsMissingPhysMatRequest())

    @unreal.ufunction(static=True)
    def log_materials_using_translucency():
        mediator.send(LogMaterialsUsingTranslucencyRequest())

    @unreal.ufunction(static=True)
    def log_materials_using_two_sided():
        mediator.send(LogTwoSidedMaterialsRequest())

    @unreal.ufunction(static=True)
    def log_foliage_with_no_max_draw_distance():
        mediator.send(LogFoliageWithNoMaxDrawDistanceRequest())

    @unreal.ufunction(static=True)
    def log_particles_with_no_lods():
        mediator.send(LogParticlesWithNoLodRequest())

    @unreal.ufunction(static=True)
    def log_sound_cue_missing_attenuation():
        mediator.send(LogSoundCueMissingAttenuationRequest())

    @unreal.ufunction(static=True)
    def log_sound_cue_missing_concurrency():
        mediator.send(LogSoundCueMissingConcurrencyRequest())

    @unreal.ufunction(static=True)
    def log_sound_cue_missing_sound_class():
        mediator.send(LogSoundCueMissingSoundClassRequest())

    @unreal.ufunction(static=True)
    def log_static_mesh_with_no_lod():
        mediator.send(LogStaticMeshWithNoLodRequest())

    @unreal.ufunction(static=True)
    def log_static_mesh_with_no_collision():
        mediator.send(LogStaticMeshWithNoCollisionRequest())

    @unreal.ufunction(static=True, params=[int])
    def log_static_mesh_num_of_materials(materialCount):
        mediator.send(LogStaticMeshWithXMaterialsRequest(materialCount))

    @unreal.ufunction(static=True, params=[int])
    def log_static_mesh_has_multiple_uv_channels(uvCount):
        mediator.send(LogStaticMeshHasMultipleUvChannelsRequest(uvCount))

    @unreal.ufunction(static=True)
    def log_skel_mesh_with_no_lods():
        mediator.send(LogSkelMeshWithNoLodRequest())

    @unreal.ufunction(static=True, params=[int])
    def log_skel_mesh_with_num_materials(materialCount):
        mediator.send(LogSkelMeshWithXMaterialsRequest(materialCount))

    @unreal.ufunction(static=True)
    def log_skel_mesh_missing_physics_asset():
        mediator.send(LogSkelkMeshMissingPhysicsAssetRequest())

    @unreal.ufunction(static=True, params=[ImportAssetStruct], ret=unreal.Array(ImportedAssetData))
    def preview_assets(importAssetDto: ImportAssetStruct):
        result = mediator.send(ImportAssetRequest(dto=importAssetDto))
        return result

    @unreal.ufunction(static=True, params=[unreal.Array(ImportedAssetData)])
    def import_assets(assetsToImport: unreal.Array(ImportedAssetData)):
        with unreal.ScopedEditorTransaction("Import Assets"):
            result = mediator.send(AssetsSelectedRequest(assetsToImport=assetsToImport))
            return result