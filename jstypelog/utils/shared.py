from pathlib import Path

INSTALLATION_TIMEOUT = 600
EXECUTION_TIMEOUT = 60

ASSETS_PATH = Path(__file__).parent.parent.parent / "assets"
DECLARATION_SCRIPTS_PATH = ASSETS_PATH / "declaration"
COMPARISON_SCRIPTS_PATH = ASSETS_PATH / "comparison"
EVALUATION_PATH = Path("evaluation")
PACKAGES_PATH = Path("packages")
DATA_PATH = Path("data")
DATA_JSON_PATH = DATA_PATH / "data.json"
LOGS_PATH = Path("logs")
EXAMPLES_PATH = Path("examples")
DECLARATIONS_PATH = Path("declarations")
COMPARISONS_PATH = Path("comparisons")
CACHE_PATH = Path("cache")
TEMPLATE_PATH = CACHE_PATH / "template"
PLAYGROUND_PATH = CACHE_PATH / "playground"
EXTRACTION_PATH = Path("extraction")
GENERATION_PATH = Path("generation")
COMBINED_EXTRACTION_PATH = Path(f"combined_extraction")
COMBINED_GENERATION_PATH = Path(f"combined_generation")
COMBINED_ALL_PATH = Path(f"combined_all")
BASIC_MODE_PATHS = [EXTRACTION_PATH, GENERATION_PATH]
COMBINED_MODE_PATHS = [COMBINED_EXTRACTION_PATH, COMBINED_GENERATION_PATH, COMBINED_ALL_PATH]
ALL_MODE_PATHS = BASIC_MODE_PATHS + COMBINED_MODE_PATHS
RUN_TIME_ANALYZER_PATH = Path("run-time-information-analyzer")
DECLARATION_GENERATOR_PATH = Path("ts-declaration-file-generator")
DEFINITELY_TYPED_PATH = Path("DefinitelyTyped")
NPM_TOOLS_PATH = Path("npm-tools")
TRANSPILE_PATH = NPM_TOOLS_PATH / "transpile.js"
REPOSITORY_PATH = CACHE_PATH / "repository"
PACKAGE_JSON_PATH = DATA_PATH / "package.json"
README_PATH = DATA_PATH / "README.md"
MAIN_PATH = DATA_PATH / "index.js"
TESTS_PATH = DATA_PATH / "tests"

class PackageDataMissingError(Exception):
    pass

class PackageInstallationError(Exception):
    pass

class CommonJSUnsupportedError(Exception):
    pass

class ES5UnsupportedError(Exception):
    pass

class LLMRejectedError(Exception):
    pass