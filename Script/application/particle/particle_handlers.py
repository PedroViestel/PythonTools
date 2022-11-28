from domain.particle_service import ParticleService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import ParticlesWithNoLODsMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
import unreal

class ParticleHandler:
    def __init__(self, _particleService: ParticleService, _repository: BaseRepository, _logging: BaseLogging):
        self.particleService = _particleService
        self.repository = _repository
        self.logging = _logging

    def log_particles_with_no_lods(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.particleService.particles_has_no_lods(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(ParticlesWithNoLODsMessage().build_log_summary(logStringsArray))