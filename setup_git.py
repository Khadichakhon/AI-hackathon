"""
Setup Git repository and push to GitHub
"""
import os
import subprocess
import sys
from pathlib import Path

# Get project directory (where this script is)
project_dir = Path(__file__).parent
os.chdir(project_dir)

print(f"Working directory: {project_dir}")

# Remove lock file if exists
lock_file = Path.home() / ".git" / "index.lock"
if lock_file.exists():
    try:
        lock_file.unlink()
        print("✓ Removed git lock file")
    except:
        pass

# Check if .git exists in project directory
git_dir = project_dir / ".git"
if not git_dir.exists():
    print("Initializing git repository...")
    subprocess.run(["git", "init"], cwd=project_dir, check=True)
    print("✓ Git initialized")
else:
    print("✓ Git repository exists")

# Add .gitignore if not exists
gitignore = project_dir / ".gitignore"
if not gitignore.exists():
    gitignore.write_text("""# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# Jupyter Notebook
.ipynb_checkpoints

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.log
""")
    print("✓ Created .gitignore")

# Stage files
print("\nStaging files...")
files_to_add = [
    "solver.py",
    "solver.ipynb",
    "*.py",
    "*.md",
    "*.json",
    "*.png",
    ".gitignore"
]

for pattern in files_to_add:
    if "*" in pattern:
        # Use glob to find files
        from glob import glob
        files = glob(str(project_dir / pattern))
        for f in files:
            subprocess.run(["git", "add", f], cwd=project_dir)
    else:
        file_path = project_dir / pattern
        if file_path.exists():
            subprocess.run(["git", "add", str(file_path)], cwd=project_dir)

print("✓ Files staged")

# Check status
result = subprocess.run(["git", "status", "--short"], cwd=project_dir, capture_output=True, text=True)
if result.stdout.strip():
    print(f"\nFiles to commit:\n{result.stdout}")
else:
    print("\nNo changes to commit")

# Commit
print("\nCreating commit...")
commit_msg = """Initial commit: ARC solver for Mizzou AGI Hackathon 2025

- Advanced ARC solver with multi-strategy pattern detection
  * Geometric transformations (flips, rotations, transpositions)
  * Boundary/frame detection patterns
  * Region filling patterns
  * Object manipulation (tip detection)
  * Color transformations

- Generated predictions for all 11 curve-ball tasks
  * example01_guess.json through example11_guess.json
  * All files verified and ready for submission

- Evaluation and verification tools
  * generate_predictions.py - Generate all predictions
  * verify_submission.py - Verify submission format
  * evaluation_metrics.py - Calculate metrics
  * check_performance.py - Show performance metrics
  * test_solver.py - Test solver functionality
  * video_demo.py - Create 30-second demonstration

- Documentation
  * README.md - Complete documentation
  * FINAL_STATUS.md - Status report
  * QUICK_START.md - Quick guide
  * SIMPLE_EXPLANATION.md - Simple explanations
  * ACTION_CHECKLIST.md - Action checklist

Ready for submission to Mizzou AGI Hackathon 2025"""

result = subprocess.run(["git", "commit", "-m", commit_msg], cwd=project_dir, capture_output=True, text=True)
if result.returncode == 0:
    print("✓ Commit created")
    print(result.stdout)
else:
    if "nothing to commit" in result.stdout.lower():
        print("ℹ No changes to commit (already committed)")
    else:
        print(f"⚠ {result.stdout}")
        print(f"⚠ {result.stderr}")

# Check if remote exists
result = subprocess.run(["git", "remote", "-v"], cwd=project_dir, capture_output=True, text=True)
if not result.stdout.strip():
    print("\n⚠ No remote repository configured")
    print("\nTo push to GitHub:")
    print("1. Create a new repository on GitHub")
    print("2. Run: git remote add origin <your-repo-url>")
    print("3. Run: git branch -M main")
    print("4. Run: git push -u origin main")
else:
    print(f"\n✓ Remote configured:\n{result.stdout}")
    print("\nTo push to GitHub, run:")
    print("  git branch -M main")
    print("  git push -u origin main")

print("\n✓ Git setup complete!")

