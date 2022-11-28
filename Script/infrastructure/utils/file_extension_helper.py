
from infrastructure.utils.unreal_extensions import AssetImportTypeEnum


class FileExtensionHelper():
    FILE_EXTENSIONS = {
        AssetImportTypeEnum.Meshes: ['fbx', 'obj'],
        AssetImportTypeEnum.Sounds: ['mp3', 'wma', 'aac', 'wav', 'flac'],
        AssetImportTypeEnum.Textures: ['jpeg', 'jpg', 'png', 'tga']
    }

    @staticmethod
    def get_file_formats_to_import(include_meshes: bool, include_sounds: bool, include_textures: bool):
        return (FileExtensionHelper.FILE_EXTENSIONS[AssetImportTypeEnum.Meshes] if include_meshes else []) + \
            (FileExtensionHelper.FILE_EXTENSIONS[AssetImportTypeEnum.Sounds] if include_sounds else []) + \
            (FileExtensionHelper.FILE_EXTENSIONS[AssetImportTypeEnum.Textures] if include_textures else [])

    @staticmethod
    def get_enum_with_extension(extension):
        for item in FileExtensionHelper.FILE_EXTENSIONS.keys():
            if extension in FileExtensionHelper.FILE_EXTENSIONS[item]:
                return item

        raise FileNotFoundError()