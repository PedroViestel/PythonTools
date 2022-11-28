from domain.texture_service import TextureService
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import LogTexturesAboveXSizeMessage, ValidatePowerOfTowMessage
import unreal

class TextureHandler:
    def __init__(self, _textureService: TextureService, _repository: BaseRepository, _logging: BaseLogging):
        self.textureService = _textureService
        self.repository = _repository
        self.logging = _logging

    def log_power_of_two_textures(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.textureService.validate_power_of_two_texture(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break

                ST.enter_progress_frame(1, asset)

        self.logging.log(ValidatePowerOfTowMessage().build_log_summary(logStringsArray))

    def log_textures_x_size(self, sizeOfTexToCheckAgainst):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.textureService.validate_texture_x_size(asset, sizeOfTexToCheckAgainst)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break

                ST.enter_progress_frame(1, asset)

        self.logging.log(LogTexturesAboveXSizeMessage(sizeOfTexToCheckAgainst).build_log_summary(logStringsArray))