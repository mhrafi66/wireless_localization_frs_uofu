# import logging
from .datasets import load_dataset
# from .utils import normalize
from .registry import DATASETS

# # Set up logging for your package
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("wireless_localization_frs_uofu")

__version__ = "0.1.0"
# Expose important features at the top level
__all__ = ["load_dataset", "DATASETS"]

# # Optional: Perform initialization logic (e.g., loading dataset metadata)
# logger.info("YourDataCommon initialized. Available datasets: %s", list(DATASETS.keys()))

