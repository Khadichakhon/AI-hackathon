# PowerShell script to push to GitHub
# Run this from the project directory

Write-Host "============================================================"
Write-Host "Setting up Git repository and preparing for GitHub push"
Write-Host "============================================================"

# Get project directory
$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectDir

Write-Host "`nWorking directory: $projectDir"

# Remove lock file if exists
$lockFile = "$env:USERPROFILE\.git\index.lock"
if (Test-Path $lockFile) {
    Remove-Item $lockFile -Force -ErrorAction SilentlyContinue
    Write-Host "✓ Removed git lock file"
}

# Initialize git if needed
if (-not (Test-Path ".git")) {
    Write-Host "`nInitializing git repository..."
    git init
    Write-Host "✓ Git initialized"
} else {
    Write-Host "`n✓ Git repository exists"
}

# Add .gitignore if not exists
if (-not (Test-Path ".gitignore")) {
    @"
# Python
__pycache__/
*.py[cod]
*`$py.class
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
"@ | Out-File -FilePath ".gitignore" -Encoding UTF8
    Write-Host "✓ Created .gitignore"
}

# Stage all project files
Write-Host "`nStaging files..."
git add solver.py solver.ipynb *.py *.md *.json *.png .gitignore 2>&1 | Out-Null

# Check status
Write-Host "`nFiles staged:"
git status --short | Select-Object -First 20

# Commit
Write-Host "`nCreating commit..."
$commitMsg = @"
Initial commit: ARC solver for Mizzou AGI Hackathon 2025

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

Ready for submission to Mizzou AGI Hackathon 2025
"@

git commit -m $commitMsg

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ Commit created successfully!"
    
    # Check remote
    $remote = git remote -v
    if ($remote) {
        Write-Host "`n✓ Remote configured:"
        Write-Host $remote
        Write-Host "`nTo push to GitHub:"
        Write-Host "  git branch -M main"
        Write-Host "  git push -u origin main"
    } else {
        Write-Host "`n⚠ No remote configured"
        Write-Host "`nTo add remote and push:"
        Write-Host "  1. Create repository on GitHub"
        Write-Host "  2. Run: git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
        Write-Host "  3. Run: git branch -M main"
        Write-Host "  4. Run: git push -u origin main"
    }
} else {
    Write-Host "`n⚠ Commit failed or no changes to commit"
}

Write-Host "`n============================================================"
Write-Host "Git setup complete!"
Write-Host "============================================================"

