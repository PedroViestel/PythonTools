from infrastructure.utils.unreal_extensions import ImportAssetStruct, ImportedAssetData
import unreal

class LogEmptyFoldersRequest():
    def __init__(self, delete_file: bool):
        self.delete_file = delete_file
class LogRedirectsRequest():
    pass
class LogUnusedAssetsRequest():
    pass

# Texture
class LogPowerOfTwoTextures():
    pass
class LogTexturesXSize():
    def __init__(self, sizeOfTexToCheckAgainst: int):
        self.sizeOfTexToCheckAgainst = sizeOfTexToCheckAgainst
    pass

# Material
class LogMaterialsMissingPhysMatRequest():
    pass
class LogMaterialsUsingTranslucencyRequest():
    pass
class LogTwoSidedMaterialsRequest():
    pass

# Foliage
class LogFoliageWithNoMaxDrawDistanceRequest():
    pass

# Particle
class LogParticlesWithNoLodRequest():
    pass

# Skeleton Mesh
class LogSkelMeshWithNoLodRequest():
    pass
class LogSkelMeshWithXMaterialsRequest():
    def __init__(self, numOfMatsToCheckFor: int):
        self.numOfMatsToCheckFor = numOfMatsToCheckFor
    pass
class LogSkelkMeshMissingPhysicsAssetRequest():
    pass

# Sound Cue
class LogSoundCueMissingAttenuationRequest():
    pass
class LogSoundCueMissingConcurrencyRequest():
    pass
class LogSoundCueMissingSoundClassRequest():
    pass

# Static Mesh
class LogStaticMeshWithNoLodRequest():
    pass
class LogStaticMeshWithNoCollisionRequest():
    pass
class LogStaticMeshWithXMaterialsRequest():
    def __init__(self, numOfMatsToCheckFor: int):
        self.numOfMatsToCheckFor = numOfMatsToCheckFor
    pass
class LogStaticMeshHasMultipleUvChannelsRequest():
    def __init__(self, numOfChannelsToCheckFor: int):
        self.numOfChannelsToCheckFor = numOfChannelsToCheckFor
    pass
class ImportAssetRequest():
    def __init__(self, dto: ImportAssetStruct):
        self.importAssetStruct = dto
    pass
class AssetsSelectedRequest():
    def __init__(self, assetsToImport: unreal.Array(ImportedAssetData)):
        self.assetsToImport = assetsToImport
    pass