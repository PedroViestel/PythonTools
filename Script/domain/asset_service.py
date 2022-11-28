from application.shared.result import Result
from domain.entity.asset_data import AssetData, ObjectRedirectorAssetData
from infrastructure.configuration.path_manager import PathManager
from unreal import EditorAssetLibrary

class AssetService():
    def __init__(self, _editorAssetLibrary: EditorAssetLibrary):
        self.editorAssetLibrary = _editorAssetLibrary

    def get_empty_folders(self):
        include_subfolders = True
        assets = self.editorAssetLibrary.list_assets(PathManager.get_source_dir(), recursive=include_subfolders, include_folder=True)
        folders = [asset for asset in assets if self.editorAssetLibrary.does_directory_exist(asset)]
        return folders

    def check_folder_is_empty(self, folder, delete) -> Result:
        result = Result()

        if self.editorAssetLibrary.does_directory_have_assets(folder):
            return result

        if delete:
            self.editorAssetLibrary.delete_directory(folder)
            result.message = ("Folder {} without assets was deleted".format(folder))
        else:
            result.message = ("Folder {} is empty".format(folder))

        return result

    def is_asset_being_used(self, asset) -> Result:
        assetData = AssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()
        dependencies = self.editorAssetLibrary.find_package_referencers_for_asset(asset, True)

        if len(dependencies) <= 0:
            result.message = ("        %s ------------> At Path: %s \n" % (assetData.assetName, assetData.assetPathName))

        return result

    def is_redirects(self, asset) -> Result:
        asset = ObjectRedirectorAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if asset.is_object_redirector():
            result.message = ("        %s ------------> At Path: %s \n" % (asset.assetName, asset.assetPathName))

        return result