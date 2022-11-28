import unreal

@unreal.uclass()
class UnrealGlobalEditorUtilityBase(unreal.GlobalEditorUtilityBase):
    pass

@unreal.uclass()
class UnrealEditorUtilityLibrary(unreal.EditorUtilityLibrary):
    pass

@unreal.uclass()
class UnrealEditorAssetLibrary(unreal.EditorAssetLibrary):
    pass

@unreal.uclass()
class UnrealSystemLibrary(unreal.SystemLibrary):
    pass

@unreal.uclass()
class UnrealStringLibrary(unreal.StringLibrary):
    pass

@unreal.uclass()
class UnrealEditorSkeletalMeshLibrary(unreal.EditorSkeletalMeshLibrary):
    pass

@unreal.uclass()
class UnrealEditorStaticMeshLibrary(unreal.EditorStaticMeshLibrary):
    pass

@unreal.uenum()
class AssetImportTypeEnum(unreal.EnumBase):
    Meshes = unreal.uvalue(0)
    Textures = unreal.uvalue(1)
    Sounds = unreal.uvalue(2)

@unreal.ustruct()
class ImportAssetStruct(unreal.StructBase):
    asset_path = unreal.uproperty(str)
    import_meshes = unreal.uproperty(bool)
    import_sounds = unreal.uproperty(bool)
    import_textures = unreal.uproperty(bool)

@unreal.ustruct()
class ImportedAssetData(unreal.StructBase):
    asset_name = unreal.uproperty(str)
    asset_path = unreal.uproperty(str)
    asset_destination = unreal.uproperty(str)
    asset_extension = unreal.uproperty(str)
    asset_type = unreal.uproperty(AssetImportTypeEnum)