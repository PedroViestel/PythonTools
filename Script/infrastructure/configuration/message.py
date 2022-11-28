from abc import ABC
from dataclasses import dataclass
import unreal

@dataclass
class Message(ABC):

    titleOfOptimisation: str = ""
    descOfOptimisation: str = ""
    summaryMessageIntro: str = ""
    LogStringsArray = []

    def build_log_summary(self, messages: list[str]) -> list[str]:
        self.LogStringsArray.clear()

        self.LogStringsArray.append("OPTIMISING SCRIPT \n")
        self.LogStringsArray.append("==================================================================================================== \n")
        self.LogStringsArray.append("    SCRIPT NAME: %s \n" % self.titleOfOptimisation)
        self.LogStringsArray.append("    DESCRIPTION: %s \n" % self.descOfOptimisation)
        self.LogStringsArray.append("==================================================================================================== \n \n")

        unreal.log_warning(self.titleOfOptimisation)
        unreal.log_warning(self.descOfOptimisation)

        if len(messages) <= 0:
            self.LogStringsArray.append(" -- NONE FOUND -- \n \n")
        else:
            for i in messages:
                self.LogStringsArray.append(i)

        self.LogStringsArray.append("\n")
        self.LogStringsArray.append("======================================================================================================= \n")
        self.LogStringsArray.append("    SUMMARY: \n")
        self.LogStringsArray.append("        %s \n" % self.summaryMessageIntro)
        self.LogStringsArray.append("              Found: %s \n \n" % len(messages))
        self.LogStringsArray.append("======================================================================================================= \n")

        return self.LogStringsArray

@dataclass
class ValidatePowerOfTowMessage(Message):
    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Textures That Are Not Power Of Two"
        self.descOfOptimisation = "Searches the entire project for textures that are not a power of two e.g. 13x64, 100x96 etc. Instead of e.g. 32x32, 128x128 512x256"
        self.summaryMessageIntro = "-- Textures Which Are Not A Power Of Two --"

@dataclass
class LogTexturesAboveXSizeMessage(Message):

    sizeOfTexToCheckAgainst: str = ""

    def __init__(self, _sizeOfTexToCheckAgainst):
        super().__init__(self)
        self.sizeOfTexToCheckAgainst = _sizeOfTexToCheckAgainst
        self.titleOfOptimisation = "Log Textures That Are Equal To X Size"
        self.descOfOptimisation = "Searches the entire project for Textures which are equal to the size you have set. Use to help find textures which are larger than what you need them for"
        self.summaryMessageIntro = "-- Textures Of Size %s  --" % self.sizeOfTexToCheckAgainst

@dataclass
class LogStaticMeshNumOfMaterialsMessage(Message):
    numOfMatsToCheckFor: str = ""

    def __init__(self, _numOfMatsToCheckFor):
        super().__init__(self)
        self.numOfMatsToCheckFor = _numOfMatsToCheckFor
        self.titleOfOptimisation = "LOG Static Meshes Assets With X Num Of Materials"
        self.descOfOptimisation = "Searches the entire project for static mesh assets that have a material count above the value that you have set"
        self.summaryMessageIntro = "-- Static Mesh Assets With Material Count Numbering >= %s --" % self.numOfMatsToCheckFor

@dataclass
class LogStaticMeshUVchannelsMessage(Message):
    numOfChannelsToCheckFor: str = ""

    def __init__(self, _numOfChannelsToCheckFor):
        super().__init__(self)
        self.numOfChannelsToCheckFor = _numOfChannelsToCheckFor
        self.titleOfOptimisation = "Log Static Mesh UV Channel Count For LOD 0"
        self.descOfOptimisation = "Searches the entire project for static mesh assets that have a UV channel count above the value that you have set"
        self.summaryMessageIntro = "-- Static Mesh Assets With UV Channels Numbering >= %s --" % self.numOfChannelsToCheckFor

@dataclass
class LogSkelMeshesNumOfMaterialsMessage(Message):
    numOfMatsToCheckFor: str = ""

    def __init__(self, _numOfMatsToCheckFor):
        super().__init__(self)
        self.numOfMatsToCheckFor = _numOfMatsToCheckFor
        self.titleOfOptimisation = "LOG Skeletal Mesh Assets With X Num Of Materials"
        self.descOfOptimisation = "Searches the entire project for skeletal mesh assets that have a material count above the value that you have set"
        self.summaryMessageIntro = "-- Skeletal Mesh Assets With Material Count Numbering >= %s --" % self.numOfMatsToCheckFor

@dataclass
class LogMaterialsMissingPhysMatsMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Materials With Missing Physical Materials"
        self.descOfOptimisation = "Searches the entire project for materials that don't have a phys mats plugged in"
        self.summaryMessageIntro = "-- Materials Without Phys Mats Plugged In --"

@dataclass
class LogMaterialsUsingTranslucencyMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Materials Using Translucency"
        self.descOfOptimisation = "Searches the entire project for materials that are using Translucency (master materials only, does not check material instances)"
        self.summaryMessageIntro = "-- Materials Using Translucency --"

@dataclass
class OptimiseScriptLogMaterialsUsingTwoSidedMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Materials Using Two Sided"
        self.descOfOptimisation = "Searches the entire project for materials that are using Two Sided (master materials only, does not check material instances)"
        self.summaryMessageIntro = "-- Materials Using Two Sided --"

@dataclass
class LogFoliageWithNoMaxDrawDistanceMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Foliage Asset With No Max Draw Distance Set"
        self.descOfOptimisation = "Searches the entire project for Foliage assets which have no max draw distance set"
        self.summaryMessageIntro = "-- Foliage Asset With No Max Draw Distance Set --"

@dataclass
class ParticlesWithNoLODsMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Particles With No LODs"
        self.descOfOptimisation = "Searches the entire project for particles that have no LODs setup"
        self.summaryMessageIntro = "-- Particles With No LODs --"

@dataclass
class SoundCueMissingAttenuationMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Sound Cues With Missing Attenuation Assets"
        self.descOfOptimisation = "Searches the entire project for Sound Cues that have no attenuation plugged in and also no Attenuation override set to true"
        self.summaryMessageIntro = "-- Sound Cues With No Attenuation Settings --"

@dataclass
class SoundCueMissingConcurrencyMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Sound Cues With Missing Concurrency Settings"
        self.descOfOptimisation = "Searches the entire project for Sound Cues that have no concurrency asset plugged in and also no concurrency override set to true"
        self.summaryMessageIntro = "-- Sound Cues With No Concurrency Settings --"

@dataclass
class SoundCueMissingSoundClassMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Sound Cues With Missing Sound Class"
        self.descOfOptimisation = "Searches the entire project for Sound Cues that are missing Sound Class Asset or are using the Engines Default Sound class asset"
        self.summaryMessageIntro = "-- Sound Cues With Missing Sound Class --"

@dataclass
class LogDeleteEmptyFolderMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Delete Empty Folders"
        self.descOfOptimisation = "Searches the entire project for empty folders, and log or delete the folder"
        self.summaryMessageIntro = "-- Folders With no content inside, consider deleting --"

@dataclass
class LogUnusedAssetMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Unused Project Assets"
        self.descOfOptimisation = "Searches the entire project for assets that have 0 references, that we could consider deleting"
        self.summaryMessageIntro = "-- Assets With 0 References That We Could Consider Deleting --"

@dataclass
class LogRedirectsMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log Redirects"
        self.descOfOptimisation = "Searches entire project for redirects that need fixing up (only logs doesnt perform the fix-up)"
        self.summaryMessageIntro = "-- Redirects That Could Be Fixed Up --"

@dataclass
class LogStaticMeshesNoLodMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log No LODs On Static Meshes"
        self.descOfOptimisation = "Searches the entire project for static mesh assets that do not have any LODs setup"
        self.summaryMessageIntro = "-- Static Mesh Assets Which Do Not Have any LODs Setup --"

@dataclass
class LogStaticMeshesWithNoCollisionMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log No Collision Static Meshes"
        self.descOfOptimisation = "Searches the entire project for static mesh assets that do not have any collision setup"
        self.summaryMessageIntro = "-- Static Mesh Assets Which Do Not Have Collision --"

@dataclass
class LogSkelMeshesNoLodMessage(Message):

    def __init__(self):
        super().__init__(self)
        self.titleOfOptimisation = "Log No LODs On Skeletal Meshes"
        self.descOfOptimisation = "Searches the entire project for skeletal mesh assets that do not have any LODs setup"
        self.summaryMessageIntro = "-- Skeletal Mesh Assets Which Do Not Have any LODs Setup --"

@dataclass
class ImportedFilesMessage(Message):

    def __init__(self):
        super().__init__(self)

        self.titleOfOptimisation = "Log Imported Files in folder"
        self.descOfOptimisation = "Searches the folder for files that match the types to import"
        self.summaryMessageIntro = "-- Imported Files --"