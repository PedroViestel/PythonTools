import infrastructure.cross_cutting.ioc_container as ioc_container
from mediatr import Mediator
from infrastructure.cross_cutting.package_solver import PackageSolver
import unreal
from infrastructure.configuration.request import *

ioc_container = ioc_container.Container()
_PYTHON_INTERPRETER_PATH = unreal.get_interpreter_executable_path()

class Bootstrapper():

    def __init__(self, install_missing_packages: bool = False) -> None:
        if install_missing_packages:
            PackageSolver.install_missing_packages()

    mediator = Mediator()

    def get_mediator(self):
        return self.mediator

    @Mediator.handler
    def log_empty_folders_handler(request: LogEmptyFoldersRequest):
        ioc_container.maintenance_handler().log_empty_folders(request.delete_file)
    Mediator.register_handler(log_empty_folders_handler)

    @Mediator.handler
    def log_unused_assets_handler(request: LogUnusedAssetsRequest):
        ioc_container.maintenance_handler().log_unused_assets()
    Mediator.register_handler(log_unused_assets_handler)

    @Mediator.handler
    def log_redirects_handler(request: LogRedirectsRequest):
        ioc_container.maintenance_handler().log_redirects()
    Mediator.register_handler(log_redirects_handler)

    @Mediator.handler
    def log_power_of_two_textures_handler(request: LogPowerOfTwoTextures):
        ioc_container.texture_handler().log_power_of_two_textures()
    Mediator.register_handler(log_power_of_two_textures_handler)

    @Mediator.handler
    def log_textures_x_size_handler(request: LogTexturesXSize):
        ioc_container.texture_handler().log_textures_x_size(request.sizeOfTexToCheckAgainst)
    Mediator.register_handler(log_textures_x_size_handler)

    @Mediator.handler
    def log_materials_missing_phys_mats_handler(request: LogMaterialsMissingPhysMatRequest):
        ioc_container.material_handler().log_materials_missing_phys_mats()
    Mediator.register_handler(log_materials_missing_phys_mats_handler)

    @Mediator.handler
    def log_materials_using_translucency_handler(request: LogMaterialsUsingTranslucencyRequest):
        ioc_container.material_handler().log_materials_using_translucency()
    Mediator.register_handler(log_materials_using_translucency_handler)

    @Mediator.handler
    def log_materials_using_two_sided_handler(request: LogTwoSidedMaterialsRequest):
        ioc_container.material_handler().log_materials_using_two_sided()
    Mediator.register_handler(log_materials_using_two_sided_handler)

    @Mediator.handler
    def log_foliage_with_no_max_draw_distance_handler(request: LogFoliageWithNoMaxDrawDistanceRequest):
        ioc_container.foliage_handler().log_foliage_with_no_max_draw_distance()
    Mediator.register_handler(log_foliage_with_no_max_draw_distance_handler)

    @Mediator.handler
    def log_particles_with_no_lods_handler(request: LogParticlesWithNoLodRequest):
        ioc_container.particle_handler().log_particles_with_no_lods()
    Mediator.register_handler(log_particles_with_no_lods_handler)

    @Mediator.handler
    def log_sound_cue_missing_attenuation_handler(request: LogSoundCueMissingAttenuationRequest):
        ioc_container.sound_handler().log_sound_cue_missing_attenuation()
    Mediator.register_handler(log_sound_cue_missing_attenuation_handler)

    @Mediator.handler
    def log_sound_cue_missing_concurrency_handler(request: LogSoundCueMissingConcurrencyRequest):
        ioc_container.sound_handler().log_sound_cue_missing_concurrency()
    Mediator.register_handler(log_sound_cue_missing_concurrency_handler)

    @Mediator.handler
    def log_sound_cue_missing_sound_class_handler(request: LogSoundCueMissingSoundClassRequest):
        ioc_container.sound_handler().log_sound_cue_missing_sound_class()
    Mediator.register_handler(log_sound_cue_missing_sound_class_handler)

    @Mediator.handler
    def log_static_mesh_with_no_lod_handler(request: LogStaticMeshWithNoLodRequest):
        ioc_container.static_mesh_handler().log_static_mesh_with_no_lod()
    Mediator.register_handler(log_static_mesh_with_no_lod_handler)

    @Mediator.handler
    def log_static_mesh_with_no_collision_handler(request: LogStaticMeshWithNoCollisionRequest):
        ioc_container.static_mesh_handler().log_static_mesh_with_no_collision()
    Mediator.register_handler(log_static_mesh_with_no_collision_handler)

    @Mediator.handler
    def log_static_mesh_with_x_materials_handler(request: LogStaticMeshWithXMaterialsRequest):
        ioc_container.static_mesh_handler().log_static_mesh_with_x_materials(request.numOfMatsToCheckFor)
    Mediator.register_handler(log_static_mesh_with_x_materials_handler)

    @Mediator.handler
    def log_static_mesh_has_multiple_uv_channels_handler(request: LogStaticMeshHasMultipleUvChannelsRequest):
        ioc_container.static_mesh_handler().log_static_mesh_has_multiple_uv_channels(request.numOfChannelsToCheckFor)
    Mediator.register_handler(log_static_mesh_has_multiple_uv_channels_handler)

    @Mediator.handler
    def log_skel_mesh_with_no_lods_handler(request: LogSkelMeshWithNoLodRequest):
        ioc_container.skel_mesh_handler().log_skel_mesh_with_no_lods()
    Mediator.register_handler(log_skel_mesh_with_no_lods_handler)

    @Mediator.handler
    def log_skel_mesh_with_x_materials_handler(request: LogSkelMeshWithXMaterialsRequest):
        ioc_container.skel_mesh_handler().log_skel_mesh_with_x_materials(request.numOfMatsToCheckFor)
    Mediator.register_handler(log_skel_mesh_with_x_materials_handler)

    @Mediator.handler
    def log_skel_mesh_missing_physics_asset_handler(request: LogSkelkMeshMissingPhysicsAssetRequest):
        ioc_container.skel_mesh_handler().log_skel_mesh_missing_physics_asset()
    Mediator.register_handler(log_skel_mesh_missing_physics_asset_handler)

    @Mediator.handler
    def preview_assets_handler(request: ImportAssetRequest):
        return ioc_container.import_asset_handler().preview_assets(request.importAssetStruct)
    Mediator.register_handler(preview_assets_handler)

    @Mediator.handler
    def import_assets_handler(request: AssetsSelectedRequest):
        return ioc_container.import_asset_handler().import_assets(request.assetsToImport)
    Mediator.register_handler(import_assets_handler)

    @Mediator.behavior
    def refresh_behavior(request: object, next):
        import limeade
        limeade.refresh()
        return next()
