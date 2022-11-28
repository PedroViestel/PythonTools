from infrastructure.logging.base_logging import BaseLogging
import unreal

class UnrealLogging(BaseLogging):

    def log(self, message):
        if isinstance(message, str):
            unreal.log(message)
        elif isinstance(message, list[str]):
            for x in message:
                unreal.log(x)