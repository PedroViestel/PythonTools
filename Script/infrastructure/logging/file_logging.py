from infrastructure.logging.base_logging import BaseLogging
from infrastructure.configuration.path_manager import PathManager
import unreal
import os

class FileLogging(BaseLogging):

    def log(self, message):
        logFilePath = PathManager.get_file_log_path()

        if unreal.Paths.file_exists(logFilePath):
            os.remove(logFilePath)
            unreal.log_warning("Removing file")

        with open(logFilePath, "a+") as file_object:
            if isinstance(message, list) and len(message) > 0:
                for a in message:
                    file_object.write(a)
            elif isinstance(message, str):
                file_object.write(message)
            else:
                file_object.write("No message to show")

            os.startfile(logFilePath)