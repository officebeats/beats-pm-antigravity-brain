"""
Structural Integrity Tests (v3.1.0)
System Tests for Beats PM Brain.
Verifies file structure, config validity, and skill integrity.
"""

import unittest
import sys
import os

class TestSystemStructure(unittest.TestCase):
    
    def setUp(self):
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    def test_root_directories(self):
        """Verify required root directories exist."""
        required = [
            "0. Incoming",
            "1. Company",
            "2. Products",
            "3. Meetings",
            "4. People",
            "5. Trackers",
            ".gemini"
        ]
        for d in required:
            path = os.path.join(self.root, d)
            self.assertTrue(os.path.isdir(path), f"Missing directory: {d}")
            
    def test_critical_files(self):
        """Verify critical files exist."""
        required = [
            "KERNEL.md",
            "README.md",
            "SETTINGS.md",
            "STATUS.md"
        ]
        for f in required:
            path = os.path.join(self.root, f)
            self.assertTrue(os.path.exists(path), f"Missing file: {f}")

    def test_skills_architecture(self):
        """Verify .gemini/skills structure."""
        skills_root = os.path.join(self.root, ".gemini", "skills")
        self.assertTrue(os.path.isdir(skills_root))
        
        # Check specific critical skills
        critical_skills = [
            "core-utility",
            "bug-chaser",
            "daily-synth",
            "meeting-synth",
            "prd-author"
        ]
        
        for skill in critical_skills:
            skill_path = os.path.join(skills_root, skill)
            self.assertTrue(os.path.isdir(skill_path), f"Missing skill: {skill}")
            self.assertTrue(os.path.exists(os.path.join(skill_path, "SKILL.md")), f"Missing SKILL.md for {skill}")

    def test_skill_config_validity(self):
        """Verify SKILL.md files have valid frontmatter."""
        skills_root = os.path.join(self.root, ".gemini", "skills")
        
        for skill_dir in os.listdir(skills_root):
            if skill_dir.startswith('.'): continue
            
            skill_path = os.path.join(skills_root, skill_dir, "SKILL.md")
            if os.path.exists(skill_path):
                with open(skill_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Check for YAML frontmatter
                self.assertTrue(content.startswith('---'), f"Invalid frontmatter start in {skill_dir}")
                try:
                    # Manual parsing to avoid pyyaml dependency
                    frontmatter = content.split('---')[1]
                    
                    has_name = False
                    has_desc = False
                    
                    for line in frontmatter.split('\n'):
                        if line.strip().startswith('name:'): has_name = True
                        if line.strip().startswith('description:'): has_desc = True
                        
                    self.assertTrue(has_name, f"Missing name in {skill_dir}")
                    self.assertTrue(has_desc, f"Missing description in {skill_dir}")
                except Exception as e:
                    self.fail(f"Frontmatter parsing failed for {skill_dir}: {e}")

    def test_templates_hierarchy(self):
        """Verify template folder structure."""
        templates_root = os.path.join(self.root, ".gemini", "templates")
        self.assertTrue(os.path.isdir(templates_root))
        
        required_dirs = ["daily", "docs", "meetings", "trackers"]
        for d in required_dirs:
            path = os.path.join(templates_root, d)
            self.assertTrue(os.path.isdir(path), f"Missing template category: {d}")

    def test_flattened_trackers(self):
        """Verify trackers are at the root of 5. Trackers/."""
        trackers_root = os.path.join(self.root, "5. Trackers")
        
        required = [
            "BUG_TRACKER.md",
            "PROJECT_TRACKER.md",
            "BOSS_REQUESTS.md"
        ]
        
        for f in required:
            path = os.path.join(trackers_root, f)
            self.assertTrue(os.path.exists(path), f"Missing tracker: {f}")

if __name__ == '__main__':
    unittest.main()
