from domain.import_asset_service import ImportAssetService
from infrastructure.configuration.message import ImportedFilesMessage
from infrastructure.logging.base_logging import BaseLogging
from infrastructure.utils.unreal_extensions import AssetImportTypeEnum, ImportAssetStruct, ImportedAssetData
import unreal

class ImportAssetHandler:
    def __init__(self, _importAssetService: ImportAssetService, _logging: BaseLogging):
        self.importAssetService = _importAssetService
        self.logging = _logging

    def preview_assets(self, importAssetDto: ImportAssetStruct) -> unreal.Array(ImportedAssetData):
        return self.importAssetService.preview_assets(importAssetDto)

    def import_assets(self, assets: unreal.Array(ImportedAssetData)):
        tasks = []

        meshes = self.filter_by_import_type(assets, AssetImportTypeEnum.Meshes)
        if len(meshes) > 0:
            tasks.extend(self.importAssetService.create_meshes(meshes))

        sounds = self.filter_by_import_type(assets, AssetImportTypeEnum.Sounds)
        if len(sounds) > 0:
            tasks.extend(self.importAssetService.create_sounds(sounds))

        textures = self.filter_by_import_type(assets, AssetImportTypeEnum.Textures)
        if len(textures) > 0:
            tasks.extend(self.importAssetService.create_textures(textures))

        if len(tasks) > 0:
            self.importAssetService.import_files(tasks)

        self.logging.log(ImportedFilesMessage().build_log_summary(self.transform_tasks_into_log(tasks)))

    def filter_by_import_type(self, assetsToImport: unreal.Array(ImportedAssetData), import_type: AssetImportTypeEnum):
        result = []
        asset: ImportedAssetData

        for asset in assetsToImport:
            if asset.asset_type.value == import_type.value:
                result.append(asset)

        return result

    def transform_tasks_into_log(self, tasks):
        logStringsArray = []

        task: unreal.AssetImportTask
        for task in tasks:
            logStringsArray.append("The file:{file_name} was imported at {destination} \n".format(file_name=task.get_editor_property("filename"), destination=task.get_editor_property("destination_path")))

        return logStringsArray
