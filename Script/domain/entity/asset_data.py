from dataclasses import dataclass
from typing import Any
import unreal

@dataclass
class AssetData:

    def __init__(self, assetData) -> None:
        self.asset = assetData.get_asset()
        self.assetName = self.asset.get_name()
        self.assetPathName = self.asset.get_path_name()
        self.assetClassName = self.asset.get_class().get_name()

    assetName: str
    assetPathName: str
    assetClassName: str

@dataclass
class Texture2DAssetData(AssetData):
    isValidTexture2D: bool = False
    textureXsize: int = 0
    textureYsize: int = 0

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

        if self.is_texture_2D():
            _TextureAsset = unreal.Texture2D.cast(self.asset)
            self.textureXsize = _TextureAsset.blueprint_get_size_x()
            self.textureYsize = _TextureAsset.blueprint_get_size_y()

    def is_texture_2D(self):
        return self.assetClassName == "Texture2D"


@dataclass
class MaterialAssetData(AssetData):
    phys_material: str

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

        if self.is_material_or_material_instance():
            self.phys_material = self.asset.get_editor_property("phys_material")

    def is_material(self) -> bool:
        return self.assetClassName == "Material"

    def is_material_or_material_instance(self) -> bool:
        return self.assetClassName == "Material" or self.assetClassName == "MaterialInstanceConstant"

    def get_blend_mode(self):
        return unreal.Material.cast(self.asset).blend_mode

    def is_two_sided(self):
        return self.asset.get_editor_property("phys_material")

@dataclass
class FoliageAssetData(AssetData):
    minDrawDistance: int = 0
    maxDrawDistance: int = 0

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

        if self.is_foliage():
            _FoliageAsset = self.asset.get_editor_property("cull_distance")
            self.minDrawDistance = _FoliageAsset.get_editor_property("min")
            self.maxDrawDistance = _FoliageAsset.get_editor_property("max")

    def is_foliage(self):
        return self.assetClassName == "FoliageType_InstancedStaticMesh" or self.assetClassName == "FoliageType_Actor"

@dataclass
class ParticleAssetData(AssetData):
    lod_count: int = 0

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

        if self.is_particle_system():
            self.lod_count = len(self.asset.get_editor_property("lod_settings"))

    def is_particle_system(self):
        return self.assetClassName == "ParticleSystem"

@dataclass
class SoundCueAssetData(AssetData):
    attenuation_settings: Any = None
    override_attenuation: Any = None
    concurrency_set: Any = None
    override_concurrency: Any = None
    sound_class_object: Any = None

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

        if self.is_sound_cue_system():
            _SoundCueAsset = unreal.SoundCue.cast(self.asset)
            self.attenuation_settings = _SoundCueAsset.get_editor_property("attenuation_settings")
            self.override_attenuation = _SoundCueAsset.get_editor_property("override_attenuation")
            self.concurrency_set = _SoundCueAsset.get_editor_property("concurrency_set")
            self.override_concurrency = _SoundCueAsset.get_editor_property("override_concurrency")
            self.sound_class_object = _SoundCueAsset.get_editor_property("sound_class_object")

    def is_sound_cue_system(self):
        return self.assetClassName == "SoundCue"

@dataclass
class ObjectRedirectorAssetData(AssetData):

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

    def is_object_redirector(self):
        return self.assetClassName == "ObjectRedirector"

@dataclass
class StaticMeshAssetData(AssetData):

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

    def is_static_mesh(self):
        return self.assetClassName == "StaticMesh"

@dataclass
class SkeletalMeshAssetData(AssetData):

    def __init__(self, assetData) -> None:
        super().__init__(assetData)

    def is_skeleton_mesh(self):
        return self.assetClassName == "SkeletalMesh"