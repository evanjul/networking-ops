import os
from pathlib import Path
from typing import Any, Dict


class Config:
    def __init__(self, **kwargs: Any) -> None:
        # Base configuration
        self.filename = kwargs.get("NETWORK_FILENAME", "nw-tool-default")
        self.project_root = Path(os.path.dirname(os.path.abspath(__file__)))
        self.src_dir = self.project_root / "src"

        # AWS configuration
        self.aws_access_key = None
        self.aws_secret_key = None
        self.aws_region = None

        # Process environment variables
        self._process_env_vars()
        
    def _process_env_vars(self) -> None:
        """Process environment variables to override default settings."""
        if filename_env := os.getenv("NETWORK_FILENAME"):
            self.filename = filename_env
            
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "filename": self.filename,
            "project_root": str(self.project_root),
            "src_dir": str(self.src_dir)
        }
        
    def validate(self) -> bool:
        """Validate configuration settings."""
        try:
            assert self.filename, "Filename must not be empty"
            assert self.src_dir.exists(), f"Source directory not found: {self.src_dir}"
            return True
        except AssertionError as e:
            print(f"Configuration validation failed: {e}")
            return False


# Decorator for preprocessing: this will be used to configure application settings, computer resources, etc.
# Can contain logging related to configuration loading and validation. 
def preprocess_main():
    def decorator(func):
        def wrapper(*args, **kwargs):
            config = Config()
            if not config.validate():
                raise ValueError("Invalid configuration")
            print(f"Configuration loaded: {config.to_dict()}")
            return func(config, *args, **kwargs)
        return wrapper
    return decorator