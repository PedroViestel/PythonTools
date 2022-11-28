from domain.material_service import MaterialService
from infrastructure.configuration.path_manager import PathManager
from infrastructure.configuration.message import LogMaterialsMissingPhysMatsMessage, LogMaterialsUsingTranslucencyMessage, OptimiseScriptLogMaterialsUsingTwoSidedMessage
from infrastructure.data.base_repository import BaseRepository
from infrastructure.logging.base_logging import BaseLogging
from infrastructure.utils.unreal_extensions import UnrealSystemLibrary
import unreal

class MaterialHandler:
    def __init__(self, _materialService: MaterialService, _systemLibrary: UnrealSystemLibrary, _repository: BaseRepository, _logging: BaseLogging):
        self.materialService = _materialService
        self.systemLibrary = _systemLibrary
        self.repository = _repository
        self.logging = _logging

    def log_materials_missing_phys_mats(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.materialService.is_material_missing_phys_mat(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogMaterialsMissingPhysMatsMessage().build_log_summary(logStringsArray))

    def log_materials_using_translucency(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.materialService.is_materials_using_translucency(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                """
                # material instances have no blend mode stuff exposed atm so cant do this
                elif _assetClassName == "MaterialInstanceConstant":
                    asset_obj = EditAssetLib.load_asset(asset)
                    _MaterialInstanceAsset = unreal.MaterialInstance.cast(_assetData.get_asset())
                    # unreal.log(_MaterialAsset.blend_mode)

                    if _MaterialInstanceAsset.blend_mode == unreal.BlendMode.BLEND_TRANSLUCENT:
                        LogStringsArray.append("        [MIC] %s ------------> At Path: %s \n" % (_assetName, _assetPathName))
                        # unreal.log("Asset Name: %s Path: %s \n" % (_assetName, _assetPathName))
                        # unreal.log("is a translucent material instance")
                        numOfOptimisations += 1
                """

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(LogMaterialsUsingTranslucencyMessage().build_log_summary(logStringsArray))

    def log_materials_using_two_sided(self):
        workingPath = PathManager.get_source_dir()
        allAssets = self.repository.list()
        logStringsArray = []

        with unreal.ScopedSlowTask(len(allAssets), workingPath) as ST:
            ST.make_dialog(True)

            for asset in allAssets:
                result = self.materialService.is_two_sided_material(asset)

                if result.hasMessage():
                    logStringsArray.append(result.message)

                if ST.should_cancel():
                    break
                ST.enter_progress_frame(1, asset)

        self.logging.log(OptimiseScriptLogMaterialsUsingTwoSidedMessage().build_log_summary(logStringsArray))
