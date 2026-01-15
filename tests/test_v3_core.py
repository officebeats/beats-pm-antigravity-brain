"""
Core Component Tests (v3.1.0)
Unit Tests for Beats PM System Core Scripts (Config, Utils).
"""

import unittest
import sys
import os
import tempfile
import shutil
import json

# Setup path to import from .gemini/skills/core-utility/scripts
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scripts_path = os.path.join(repo_root, ".gemini", "skills", "core-utility", "scripts")
sys.path.insert(0, scripts_path)

from utils import config
from utils import filesystem

class TestConfig(unittest.TestCase):
    
    def setUp(self):
        # Override config path to a temp file for testing
        self.test_dir = tempfile.mkdtemp()
        self.config_path = os.path.join(self.test_dir, "config.json")
        
        # Patch the get_config_path function
        self.original_get_path = config.get_config_path
        config.get_config_path = lambda: self.config_path
        
        # Reset cache
        config._config_cache = None

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        config.get_config_path = self.original_get_path
        config._config_cache = None
        
    def test_default_config_generation(self):
        """Test that loading config generates defined defaults."""
        conf = config.load_config()
        self.assertEqual(conf['system']['version'], '3.1.0')
        self.assertTrue(os.path.exists(self.config_path))
        
    def test_get_config_value(self):
        """Test retrieving nested config values."""
        val = config.get_config('paths.staging')
        self.assertEqual(val, '0. Incoming/staging')
        
    def test_set_config_value(self):
        """Test setting a config value."""
        config.set_config('ai.default_model', 'test-model-v1')
        val = config.get_config('ai.default_model')
        self.assertEqual(val, 'test-model-v1')
        
        # Verify persistence
        config._config_cache = None
        val_reloaded = config.get_config('ai.default_model')
        self.assertEqual(val_reloaded, 'test-model-v1')

class TestFilesystem(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_ensure_directory(self):
        """Test directory creation."""
        target = os.path.join(self.test_dir, "subdir", "deep")
        filesystem.ensure_directory(target)
        self.assertTrue(os.path.isdir(target))
        
    def test_write_and_read_file(self):
        """Test file I/O."""
        target = os.path.join(self.test_dir, "test.txt")
        content = "Hello World"
        
        filesystem.write_file(target, content)
        self.assertTrue(os.path.exists(target))
        
        read_content = filesystem.read_file(target)
        self.assertEqual(read_content, content)

if __name__ == '__main__':
    unittest.main()
