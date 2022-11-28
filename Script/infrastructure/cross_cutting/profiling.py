import unreal

_PYTHON_INTERPRETER_PATH = unreal.get_interpreter_executable_path()

class Profiler():
    def attach_debugger():
        import debugpy
        debugpy.configure(python=_PYTHON_INTERPRETER_PATH)
        debugpy.listen(5678)
        print('Waiting for a debugger to attach...')
        debugpy.wait_for_client()