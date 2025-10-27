namespace cAlgo.Indicators;

public static class PythonHooks
{
    public const string DummyTraceback = @"
def format_exc(limit=None, chain=True):
    return '<traceback unavailable>'

def format_tb(tb, limit=None):
    return ['<traceback unavailable (format_tb)>']

def extract_tb(tb, limit=None):
    return [('file', 0, 'func', 'line')]

def print_exc(limit=None, file=None, chain=True):
    if file:
        file.write('<traceback unavailable>\n')
    else:
        print('<traceback unavailable>')

def print_tb(tb, limit=None, file=None):
    if file:
        file.write('<traceback unavailable (tb)>\n')
    else:
        print('<traceback unavailable (tb)>')

def print_exception(exc_type, exc_value, tb, limit=None, file=None, chain=True):
    if file:
        file.write('<traceback unavailable (exception)>\n')
    else:
        print('<traceback unavailable (exception)>')
";
   public const string InMemoryModuleLoaderPythonCode = @"
import sys
import importlib.abc
import importlib.util

ENABLE_INMEMORY_IMPORT_LOGGING = False  # <- Set to True to enable logging

def log(msg):
    if ENABLE_INMEMORY_IMPORT_LOGGING:
        print(msg)

class InMemoryModuleLoader(importlib.abc.Loader):
    def __init__(self, module_code_map):
        self.module_code_map = module_code_map

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        code = self.module_code_map.get(module.__name__)
        exec(code, module.__dict__)

class InMemoryModuleFinder(importlib.abc.MetaPathFinder):
    def __init__(self, module_code_map):
        self.module_code_map = module_code_map

    def find_spec(self, fullname, path, target=None):
        try:
            log(f""[InMemoryLoader] Trying to load: {fullname}"")
        except NameError:
            log(f""[FALLBACK] {fullname}"")

        if fullname in self.module_code_map:
            log(f""[InMemoryLoader] Loaded from memory: {fullname}"")
            return importlib.util.spec_from_loader(fullname, InMemoryModuleLoader(self.module_code_map))
        return None

def install_inmemory_importer(module_map, enable_logging=False):
    global ENABLE_INMEMORY_IMPORT_LOGGING
    ENABLE_INMEMORY_IMPORT_LOGGING = enable_logging
    finder = InMemoryModuleFinder(module_map)
    sys.meta_path.insert(0, finder)
";
}