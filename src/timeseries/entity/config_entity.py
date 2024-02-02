from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path

@dataclass(frozen=True)
class PrepareDataConfig:
    data_path: Path
    train_size : float
    coll_name : str
    look_Back : int