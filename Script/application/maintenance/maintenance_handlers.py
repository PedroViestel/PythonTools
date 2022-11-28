from domain.asset_service import AssetService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import LogDeleteEmptyFolderMessage, LogRedirectsMessage, LogUnusedAssetMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
import unreal

class MaintenanceHandler:
    def __init__(self, _assetService: AssetService, _repository: BaseRepository, _logging: BaseLogging):
        self.assetService = _assetService
        self.assetRepository = _repository
        self.logging = _logging

    def log_empty_folders(self, delete_file: bool):
        folders = self.assetService.get_empty_folders()
        logStringsArray = []

        for folder in folders:
            # check if folder has assets
            result = self.assetService.check_folder_is_empty(folder, delete_file)

            if result.hasMessage():
                logStringsArray.append(result.message)

        self.logging.log(LogDeleteEmptyFolderMessage().build_log_summary(logStringsArray))

    def log_unused_assets(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.assetRepository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.assetService.is_asset_being_used(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogUnusedAssetMessage().build_log_summary(logStringsArray))

    def log_redirects(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.assetRepository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.assetService.is_redirects(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogRedirectsMessage().build_log_summary(logStringsArray))