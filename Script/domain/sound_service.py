from application.shared.result import Result
from domain.entity.asset_data import SoundCueAssetData
from unreal import EditorAssetLibrary, SystemLibrary, StringLibrary

class SoundService():
    def __init__(self, _editorAssetLibrary: EditorAssetLibrary, _systemLibrary: SystemLibrary, _stringLibrary: StringLibrary):
        self.editorAssetLibrary = _editorAssetLibrary
        self.stringLibrary = _stringLibrary
        self.systemLibrary = _systemLibrary

    def is_sound_cue_missing_attenuation(self, asset) -> Result:
        soundData = SoundCueAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if soundData.is_sound_cue_system() and not self.systemLibrary.is_valid(soundData.attenuation_settings) and not soundData.override_attenuation:
            result.message = ("        %s ------------> At Path: %s \n" % (soundData.assetName, soundData.assetPathName))

        return result

    def is_sound_cue_missing_concurrency(self, asset) -> Result:
        soundData = SoundCueAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if soundData.is_sound_cue_system() and len(soundData.concurrency_set) <= 0 and not soundData.override_concurrency:
            result.message = ("        %s ------------> At Path: %s \n" % (soundData.assetName, soundData.assetPathName))

        return result

    def is_sound_cue_missing_sound_class(self, asset) -> Result:
        soundData = SoundCueAssetData(self.editorAssetLibrary.find_asset_data(asset))
        result = Result()

        if soundData.is_sound_cue_system():
            if not self.systemLibrary.is_valid(soundData.sound_class_object):  # no Sound class asset plugged in
                result.message = ("        [No Asset Plugged in] %s ------------> At Path: %s \n" % (soundData.assetName, soundData.assetPathName))
            elif self.stringLibrary.contains(soundData.assetPathName, "Engine"):  # Sound Class Asset Plugged in but its Engine Default
                result.message = ("        [Engine Default Used] %s ------------> At Path: %s \n" % (soundData.assetName, soundData.assetPathName))

        return result