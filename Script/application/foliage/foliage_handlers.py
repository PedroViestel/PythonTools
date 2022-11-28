from domain.foliage_service import FoliageService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import LogFoliageWithNoMaxDrawDistanceMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
import unreal

class FoliageHandler:
    def __init__(self, _foliageService: FoliageService, _repository: BaseRepository, _logging: BaseLogging):
        self.foliageService = _foliageService
        self.repository = _repository
        self.logging = _logging

    def log_foliage_with_no_max_draw_distance(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.foliageService.foliage_has_max_draw_distance(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogFoliageWithNoMaxDrawDistanceMessage().build_log_summary(logStringsArray))