import unreal
class FileExtensionHelper():
    FILE_EXTENSIONS = {
        unreal.AssetImportTypeEnum.MESHES: ['fbx', 'obj'],
        unreal.AssetImportTypeEnum.SOUNDS: ['mp3', 'wma', 'aac', 'wav', 'flac'],
        unreal.AssetImportTypeEnum.TEXTURES: ['jpeg', 'jpg', 'png', 'tga']
    }

    @staticmethod
    def get_file_formats_to_import(include_meshes: bool, include_sounds: bool, include_textures: bool):
        return (FileExtensionHelper.FILE_EXTENSIONS[unreal.AssetImportTypeEnum.MESHES] if include_meshes else []) + \
            (FileExtensionHelper.FILE_EXTENSIONS[unreal.AssetImportTypeEnum.SOUNDS] if include_sounds else []) + \
            (FileExtensionHelper.FILE_EXTENSIONS[unreal.AssetImportTypeEnum.TEXTURES] if include_textures else [])

    @staticmethod
    def get_enum_with_extension(extension):
        for item in FileExtensionHelper.FILE_EXTENSIONS.keys():
            if extension in FileExtensionHelper.FILE_EXTENSIONS[item]:
                return item

        raise FileNotFoundError()