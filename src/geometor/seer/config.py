"""Handles loading and accessing application configuration from YAML files."""
from __future__ import annotations

from pathlib import Path
import yaml
from typing import Any, Dict, Optional

class ConfigError(Exception):
    """Custom exception for configuration loading errors."""
    pass

class Config:
    """
    Handles loading and accessing configuration from a specified directory.

    Expects an 'index.yaml' file in the root of the config_dir.
    Referenced files (instructions, context files) within index.yaml
    are expected to be relative to config_dir and their content
    will be loaded into the configuration data.
    """
    def __init__(self, config_dir: Path | str):
        """
        Initializes the Config object by loading data from index.yaml
        and referenced files within the specified directory.

        Args:
            config_dir: The path to the configuration directory.

        Raises:
            FileNotFoundError: If config_dir or index.yaml does not exist.
            ConfigError: If index.yaml is not valid YAML or referenced files
                         are missing or cannot be read.
        """
        self.config_dir = Path(config_dir)
        if not self.config_dir.is_dir():
            raise FileNotFoundError(f"Configuration directory not found: {self.config_dir}")

        self.index_file = self.config_dir / "index.yaml"
        if not self.index_file.is_file():
            raise FileNotFoundError(f"Configuration file not found: {self.index_file}")

        self._data: Dict[str, Any] = self._load_config_file()
        self._load_referenced_files()

    def _load_config_file(self) -> Dict[str, Any]:
        """Loads the main index.yaml file."""
        try:
            with open(self.index_file, "r") as f:
                data = yaml.safe_load(f)
                if not isinstance(data, dict):
                    raise ConfigError(f"Invalid YAML format in {self.index_file}. Expected a dictionary.")
                return data
        except yaml.YAMLError as e:
            raise ConfigError(f"Error parsing YAML file {self.index_file}: {e}") from e
        except IOError as e:
            raise ConfigError(f"Error reading configuration file {self.index_file}: {e}") from e

    def _load_referenced_files(self):
        """
        Loads the content of files referenced within the configuration data.

        Assumes file paths are relative to the config_dir.
        Modifies the internal _data dictionary, replacing filenames with content.
        """
        # Load instruction files
        if "instructions" in self._data and isinstance(self._data["instructions"], dict):
            for key, filename in list(self._data["instructions"].items()): # Iterate over a copy of items
                if isinstance(filename, str): # Only process if it looks like a filename
                    try:
                        self._data["instructions"][key] = self._read_file_content(filename, f"instruction '{key}'")
                    except ConfigError as e:
                        print(f"Warning: {e}. Skipping instruction '{key}'.")
                        # Optionally remove the key if loading failed critically
                        # del self._data["instructions"][key]
                        self._data["instructions"][key] = "" # Or set to empty string
                else:
                    print(f"Warning: Invalid filename format for instruction '{key}': {filename}. Skipping.")
                    # Keep the original value or set to empty? Let's set to empty for consistency.
                    self._data["instructions"][key] = ""

        else:
            print(f"Warning: 'instructions' section missing or invalid in {self.index_file}")
            self._data["instructions"] = {} # Ensure it exists as an empty dict

        # Load task context file
        task_context_filename = self._data.get("task_context_file")
        if task_context_filename and isinstance(task_context_filename, str):
            try:
                self._data["task_context_content"] = self._read_file_content(task_context_filename, "task context")
            except ConfigError as e:
                 print(f"Warning: {e}. Using empty task context.")
                 self._data["task_context_content"] = ""
            # del self._data["task_context_file"] # Optional: remove the old key
        else:
            print(f"Warning: 'task_context_file' missing or invalid in {self.index_file}. Using empty task context.")
            self._data["task_context_content"] = "" # Provide default empty content

        # Load system context files within roles
        if "roles" in self._data and isinstance(self._data["roles"], dict):
            for role_name, role_config in self._data["roles"].items():
                if isinstance(role_config, dict):
                    system_context_filename = role_config.get("system_context_file")
                    if system_context_filename and isinstance(system_context_filename, str):
                        try:
                            role_config["system_context_content"] = self._read_file_content(
                                system_context_filename, f"system context for role '{role_name}'"
                            )
                        except ConfigError as e:
                            print(f"Warning: {e}. Using empty system context for role '{role_name}'.")
                            role_config["system_context_content"] = ""
                        # del role_config["system_context_file"] # Optional: remove old key
                    else:
                        print(f"Warning: Invalid or missing 'system_context_file' for role '{role_name}'. Using empty system context.")
                        role_config["system_context_content"] = "" # Default empty
                else:
                     print(f"Warning: Invalid configuration for role '{role_name}'. Skipping system context loading.")
                     # Ensure role_config is a dict if we proceed, though it might indicate a larger issue
                     if not isinstance(role_config, dict):
                         self._data["roles"][role_name] = {} # Replace invalid entry? Risky.
                     # Or just skip adding system_context_content

        else:
            print(f"Warning: 'roles' section missing or invalid in {self.index_file}")
            self._data["roles"] = {} # Ensure it exists

    def _read_file_content(self, relative_path: str, description: str) -> str:
        """Reads content from a file relative to the config_dir."""
        file_path = (self.config_dir / relative_path).resolve()
        # Basic check to prevent reading files outside the config dir
        if self.config_dir.resolve() not in file_path.parents:
             raise ConfigError(f"Attempted to read file outside config directory: {relative_path}")

        try:
            with open(file_path, "r", encoding='utf-8') as f: # Specify encoding
                return f.read().strip()
        except FileNotFoundError:
            raise ConfigError(f"Missing referenced {description} file: {file_path}") from None
        except IOError as e:
            raise ConfigError(f"Error reading referenced {description} file {file_path}: {e}") from e
        except Exception as e: # Catch other potential errors like UnicodeDecodeError
            raise ConfigError(f"Unexpected error reading {description} file {file_path}: {e}") from e


    # --- Accessor Properties ---

    @property
    def data(self) -> Dict[str, Any]:
        """Returns the raw loaded configuration data dictionary."""
        # Consider returning a deep copy if mutation is a concern
        # import copy; return copy.deepcopy(self._data)
        return self._data

    @property
    def roles(self) -> Dict[str, Dict[str, Any]]:
        """Returns the roles configuration dictionary."""
        return self._data.get("roles", {})

    @property
    def instructions(self) -> Dict[str, str]:
        """Returns the instructions dictionary (keys mapped to content)."""
        return self._data.get("instructions", {})

    @property
    def task_context(self) -> str:
        """Returns the loaded task context content."""
        return self._data.get("task_context_content", "")

    @property
    def max_iterations(self) -> int:
        """Returns the max_iterations value."""
        # Provide a default value if not specified
        return self._data.get("max_iterations", 5)

    @property
    def use_images(self) -> bool:
        """Returns the use_images flag."""
        return self._data.get("use_images", False)

    # Add more properties as needed for other top-level config keys

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Provides dictionary-like get access to the top-level config."""
        return self._data.get(key, default)

    def __getitem__(self, key: str) -> Any:
        """Provides dictionary-like access to the top-level config."""
        if key not in self._data:
             raise KeyError(f"Configuration key '{key}' not found.")
        return self._data[key] # Raises KeyError if key doesn't exist

    def __contains__(self, key: str) -> bool:
        """Allows checking for key existence using 'in'."""
        return key in self._data
