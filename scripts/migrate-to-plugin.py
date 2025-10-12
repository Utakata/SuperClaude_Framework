#!/usr/bin/env python3
"""
SuperClaude v4 → v5 (Plugin) Migration Script

Usage:
  python3 migrate-to-plugin.py --check      # Check current installation
  python3 migrate-to-plugin.py --migrate    # Perform migration
  python3 migrate-to-plugin.py --rollback   # Rollback to v4
"""

import os
import shutil
import json
from pathlib import Path

class SuperClaudeMigration:
    def __init__(self):
        self.claude_dir = Path.home() / ".claude"
        self.backup_dir = Path.home() / ".claude-v4-backup"

    def check_installation(self):
        """Check current SuperClaude installation"""
        print("🔍 Checking SuperClaude installation...")

        # Check v4 installation
        v4_files = [
            self.claude_dir / "CLAUDE.md",
            self.claude_dir / "COMMANDS.md",
            self.claude_dir / "AGENTS.md"
        ]

        v4_installed = all(f.exists() for f in v4_files)

        # Check plugin installation
        plugin_manifest = self.claude_dir / ".claude-plugin" / "plugin.json"
        plugin_installed = plugin_manifest.exists()

        print(f"  v4.x Installation: {'✅ Found' if v4_installed else '❌ Not found'}")
        print(f"  Plugin Installation: {'✅ Found' if plugin_installed else '❌ Not found'}")

        return {
            "v4_installed": v4_installed,
            "plugin_installed": plugin_installed
        }

    def backup_v4(self):
        """Backup v4 installation"""
        print("💾 Creating backup of v4 installation...")

        if self.backup_dir.exists():
            shutil.rmtree(self.backup_dir)

        shutil.copytree(self.claude_dir, self.backup_dir)
        print(f"  Backup created at: {self.backup_dir}")

    def migrate_to_plugin(self):
        """Migrate from v4 to plugin format"""
        print("🚀 Migrating to plugin format...")

        # Step 1: Backup
        self.backup_v4()

        # Step 2: Uninstall v4 (keep user customizations)
        print("  Removing v4 core files...")
        v4_core_files = [
            "COMMANDS.md", "AGENTS.md", "MODES.md"
        ]
        for file in v4_core_files:
            file_path = self.claude_dir / file
            if file_path.exists():
                file_path.unlink()

        # Step 3: Instructions for plugin installation
        print("\n✅ v4 migration complete!")
        print("\n📋 Next steps:")
        print("  1. Open Claude Code")
        print("  2. Run: /plugin marketplace add SuperClaude-Org/superclaude-plugin-marketplace")
        print("  3. Run: /plugin install superclaude-framework")
        print("  4. Your custom configurations have been preserved")

    def rollback_to_v4(self):
        """Rollback to v4 if needed"""
        print("⏪ Rolling back to v4...")

        if not self.backup_dir.exists():
            print("  ❌ No backup found. Cannot rollback.")
            return

        # Remove plugin installation
        plugin_dir = self.claude_dir / ".claude-plugin"
        if plugin_dir.exists():
            shutil.rmtree(plugin_dir)

        # Restore v4 files
        for file in ["CLAUDE.md", "COMMANDS.md", "AGENTS.md", "MODES.md"]:
            src = self.backup_dir / file
            dst = self.claude_dir / file
            if src.exists():
                shutil.copy2(src, dst)

        print("  ✅ Rollback complete!")

if __name__ == "__main__":
    import sys

    migrator = SuperClaudeMigration()

    if "--check" in sys.argv:
        migrator.check_installation()
    elif "--migrate" in sys.argv:
        migrator.migrate_to_plugin()
    elif "--rollback" in sys.argv:
        migrator.rollback_to_v4()
    else:
        print(__doc__)
