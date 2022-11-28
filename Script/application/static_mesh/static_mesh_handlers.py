from domain.static_meshe_service import StaticMeshService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import LogStaticMeshesNoLodMessage, LogStaticMeshesWithNoCollisionMessage, LogStaticMeshUVchannelsMessage, LogStaticMeshNumOfMaterialsMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
import unreal

class StaticMeshHandler:
    def __init__(self, _staticMesheService: StaticMeshService, _repository: BaseRepository, _logging: BaseLogging):
        self.staticMesheService = _staticMesheService
        self.repository = _repository
        self.logging = _logging

    def log_static_mesh_with_no_lod(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.staticMesheService.mesh_has_no_lods(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogStaticMeshesNoLodMessage().build_log_summary(logStringsArray))

    def log_static_mesh_with_no_collision(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.staticMesheService.mesh_with_no_collision(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogStaticMeshesWithNoCollisionMessage().build_log_summary(logStringsArray))

    def log_static_mesh_with_x_materials(self, numOfMatsToCheckFor):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.staticMesheService.mesh_num_of_materials(asset, numOfMatsToCheckFor)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogStaticMeshNumOfMaterialsMessage(numOfMatsToCheckFor).build_log_summary(logStringsArray))

    def log_static_mesh_has_multiple_uv_channels(self, numOfChannelsToCheckFor):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.staticMesheService.mesh_has_multiple_uv_channels(asset, numOfChannelsToCheckFor)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogStaticMeshUVchannelsMessage(numOfChannelsToCheckFor).build_log_summary(logStringsArray))