from dependency_injector import containers, providers
from application.foliage.foliage_handlers import FoliageHandler
from application.import_asset.import_asset_handlers import ImportAssetHandler
from domain.import_asset_service import ImportAssetService
from application.maintenance.maintenance_handlers import MaintenanceHandler
from application.material.material_handlers import MaterialHandler
from application.particle.particle_handlers import ParticleHandler
from application.skeleton_mesh.skeleton_mesh_handlers import SkeletonMeshHandler
from application.sound.sound_handlers import SoundHandler
from application.static_mesh.static_mesh_handlers import StaticMeshHandler
from application.texture.texture_handlers import TextureHandler
from domain.asset_service import AssetService
from domain.foliage_service import FoliageService
from domain.material_service import MaterialService
from domain.particle_service import ParticleService
from domain.skeletal_meshe_service import SkeletalMeshService
from domain.sound_service import SoundService
from domain.static_meshe_service import StaticMeshService
from domain.texture_service import TextureService
from infrastructure.data.editor_repository import EditorRepository
from infrastructure.logging.file_logging import FileLogging
from infrastructure.utils.unreal_extensions import UnrealEditorAssetLibrary, UnrealEditorSkeletalMeshLibrary, UnrealEditorStaticMeshLibrary, UnrealEditorUtilityLibrary, UnrealStringLibrary, UnrealSystemLibrary

class Container(containers.DeclarativeContainer):

    logging = providers.Factory(FileLogging)

    editorUtilityLibrary = providers.Factory(UnrealEditorUtilityLibrary)
    editorAssetLibrary = providers.Factory(UnrealEditorAssetLibrary)
    systemLibrary = providers.Factory(UnrealSystemLibrary)
    stringLibrary = providers.Factory(UnrealStringLibrary)
    skeletalMeshLibrary = providers.Factory(UnrealEditorSkeletalMeshLibrary)
    staticMeshLibrary = providers.Factory(UnrealEditorStaticMeshLibrary)

    assetService = providers.Factory(AssetService, _editorAssetLibrary=editorAssetLibrary)
    textureService = providers.Factory(TextureService, _editorAssetLibrary=editorAssetLibrary)
    materialService = providers.Factory(MaterialService, _editorAssetLibrary=editorAssetLibrary, _systemLibrary=systemLibrary)
    foliageService = providers.Factory(FoliageService, _editorAssetLibrary=editorAssetLibrary)
    particleService = providers.Factory(ParticleService, _editorAssetLibrary=editorAssetLibrary)
    soundService = providers.Factory(SoundService, _editorAssetLibrary=editorAssetLibrary, _stringLibrary=stringLibrary, _systemLibrary=systemLibrary)
    skelMeshService = providers.Factory(SkeletalMeshService, _editorAssetLibrary=editorAssetLibrary, _editorSkeletalMeshLibrary=skeletalMeshLibrary, _systemLibrary=systemLibrary)
    staticMeshService = providers.Factory(StaticMeshService, _editorAssetLibrary=editorAssetLibrary, _editorStaticMeshLibrary=staticMeshLibrary)
    importAssetService = providers.Factory(ImportAssetService, _editorAssetLibrary=editorAssetLibrary)

    repository = providers.Factory(EditorRepository, _editorAssetLibrary=editorAssetLibrary)

    maintenance_handler = providers.Factory(
        MaintenanceHandler,
        _assetService=assetService,
        _repository=repository,
        _logging=logging
    )

    texture_handler = providers.Factory(
        TextureHandler,
        _textureService=textureService,
        _repository=repository,
        _logging=logging
    )

    material_handler = providers.Factory(
        MaterialHandler,
        _materialService=materialService,
        _repository=repository,
        _systemLibrary=systemLibrary,
        _logging=logging
    )

    foliage_handler = providers.Factory(
        FoliageHandler,
        _foliageService=foliageService,
        _repository=repository,
        _logging=logging
    )

    particle_handler = providers.Factory(
        ParticleHandler,
        _particleService=particleService,
        _repository=repository,
        _logging=logging
    )

    sound_handler = providers.Factory(
        SoundHandler,
        _soundService=soundService,
        _repository=repository,
        _logging=logging
    )

    static_mesh_handler = providers.Factory(
        StaticMeshHandler,
        _staticMesheService=staticMeshService,
        _repository=repository,
        _logging=logging
    )

    skel_mesh_handler = providers.Factory(
        SkeletonMeshHandler,
        _skelMeshService=skelMeshService,
        _repository=repository,
        _logging=logging
    )

    import_asset_handler = providers.Factory(
        ImportAssetHandler,
        _importAssetService=importAssetService,
        _logging=logging
    )