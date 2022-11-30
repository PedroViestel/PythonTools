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