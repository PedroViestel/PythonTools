from domain.skeletal_meshe_service import SkeletalMeshService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import LogSkelMeshesNumOfMaterialsMessage, LogSkelMeshesNoLodMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
import unreal

class SkeletonMeshHandler:
    def __init__(self, _skelMeshService: SkeletalMeshService, _repository: BaseRepository, _logging: BaseLogging):
        self.skelMeshService = _skelMeshService
        self.repository = _repository
        self.logging = _logging

    def log_skel_mesh_with_no_lods(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.skelMeshService.mesh_has_no_lods(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogSkelMeshesNoLodMessage().build_log_summary(logStringsArray))

    def log_skel_mesh_with_x_materials(self, numOfMatsToCheckFor):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.skelMeshService.mesh_num_of_materials(asset, numOfMatsToCheckFor)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogSkelMeshesNumOfMaterialsMessage(numOfMatsToCheckFor).build_log_summary(logStringsArray))

    def log_skel_mesh_missing_physics_asset(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.skelMeshService.mesh_has_no_physics_asset(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogSkelMeshesNoLodMessage().build_log_summary(logStringsArray))