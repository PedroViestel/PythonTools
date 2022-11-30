from infrastructure.configuration.path_manager import PathManager
from infrastructure.utils.file_extension_helper import FileExtensionHelper
import unreal
from typing import Protocol
from abc import abstractmethod
import os
import re

class ImportAssetService():

    def __init__(self, _editorAssetLibrary: unreal.EditorAssetLibrary):
        self.editorAssetLibrary = _editorAssetLibrary

    def create_meshes(self, files):
        return ImportAssetFactory.get_importer(unreal.AssetImportTypeEnum.MESHES).create_tasks_from_files(files)

    def create_sounds(self, files):
        return ImportAssetFactory.get_importer(unreal.AssetImportTypeEnum.SOUNDS).create_tasks_from_files(files)

    def create_textures(self, files):
        return ImportAssetFactory.get_importer(unreal.AssetImportTypeEnum.TEXTURES).create_tasks_from_files(files)

    def preview_assets(self, importAssetDto: unreal.ImportAssetStruct) -> unreal.Array(unreal.ImportedAssetData):
        files = FileProcessor().get_files_with_extensions_from_folder(importAssetDto.asset_path, FileExtensionHelper.get_file_formats_to_import(include_meshes=importAssetDto.import_meshes, include_sounds=importAssetDto.import_sounds, include_textures=importAssetDto.import_textures))
        return files

    def import_files(self, tasks):
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)

class ImportAssetBase(Protocol):

    @abstractmethod
    def get_import_asset_enum(self):
        raise NotImplementedError

    @abstractmethod
    def get_destination_folder(self):
        raise NotImplementedError

    def build_import_options(self):
        return None

    def build_import_task(self, filename, destination_path) -> unreal.AssetImportTask:
        task = unreal.AssetImportTask()
        task.set_editor_property('automated', True)
        task.set_editor_property('destination_name', '')
        task.set_editor_property('destination_path', destination_path)
        task.set_editor_property('filename', filename)
        task.set_editor_property('replace_existing', True)
        task.set_editor_property('save', False)
        task.set_editor_property('options', self.build_import_options())
        return task

    def create_tasks_from_files(self, files):
        destination_path = self.get_destination_folder()
        tasks = []

        if not unreal.Paths.directory_exists(destination_path):
            unreal.EditorAssetLibrary.make_directory(destination_path)

            file: unreal.ImportedAssetData
            for file in files:
                tasks.append(self.build_import_task(filename=file.asset_path, destination_path=file.asset_destination))

        return tasks

class MeshImporter(ImportAssetBase):
    def get_import_asset_enum(self):
        return unreal.AssetImportTypeEnum.MESHES

    def get_destination_folder(self):
        return PathManager.get_mesh_destination_folder()

    def build_import_options(self):
        options = unreal.FbxImportUI()
        options.set_editor_property('import_mesh', True)
        options.set_editor_property('import_textures', False)
        options.set_editor_property('import_materials', False)
        options.set_editor_property('import_as_skeletal', False)
        options.set_editor_property('mesh_type_to_import', unreal.FBXImportType.FBXIT_STATIC_MESH)
        return options

class SoundImporter(ImportAssetBase):
    def get_import_asset_enum(self):
        return unreal.AssetImportTypeEnum.SOUNDS

    def get_destination_folder(self):
        return PathManager.get_sound_destination_folder()

class TextureImporter(ImportAssetBase):
    def get_import_asset_enum(self):
        return unreal.AssetImportTypeEnum.TEXTURES

    def get_destination_folder(self):
        return PathManager.get_texture_destination_folder()

class ImportAssetFactory():
    FACTORIES = {
        unreal.AssetImportTypeEnum.MESHES: MeshImporter(),
        unreal.AssetImportTypeEnum.SOUNDS: SoundImporter(),
        unreal.AssetImportTypeEnum.TEXTURES: TextureImporter()
    }

    @staticmethod
    def get_importer(type: unreal.AssetImportTypeEnum) -> ImportAssetBase:
        return ImportAssetFactory.FACTORIES[type]

class FileProcessor():
    def get_files_with_extensions_from_folder(self, asset_path: str, extensions) -> unreal.Array(unreal.ImportedAssetData):
        files = unreal.Array(unreal.ImportedAssetData)

        # r=root, d=directories, f = files
        for r, d, f in os.walk(asset_path):
            for file in f:
                for extension in extensions:
                    if re.search('.' + extension, file, re.IGNORECASE):
                        newFile = unreal.ImportedAssetData()
                        newFile.asset_extension = extension
                        newFile.asset_path = os.path.join(r, file)
                        newFile.asset_name = file
                        newFile.asset_type = FileExtensionHelper.get_enum_with_extension(extension)
                        newFile.asset_destination = ImportAssetFactory.get_importer(newFile.asset_type).get_destination_folder()
                        files.append(newFile)

        return files