from domain.sound_service import SoundService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import SoundCueMissingAttenuationMessage, SoundCueMissingConcurrencyMessage, SoundCueMissingSoundClassMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
import unreal

class SoundHandler:
    def __init__(self, _soundService: SoundService, _repository: BaseRepository, _logging: BaseLogging):
        self.soundService = _soundService
        self.repository = _repository
        self.logging = _logging

    def log_sound_cue_missing_attenuation(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.soundService.is_sound_cue_missing_attenuation(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(SoundCueMissingAttenuationMessage().build_log_summary(logStringsArray))

    def log_sound_cue_missing_concurrency(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.soundService.is_sound_cue_missing_concurrency(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(SoundCueMissingConcurrencyMessage().build_log_summary(logStringsArray))

    def log_sound_cue_missing_sound_class(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.soundService.is_sound_cue_missing_sound_class(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(SoundCueMissingSoundClassMessage().build_log_summary(logStringsArray))