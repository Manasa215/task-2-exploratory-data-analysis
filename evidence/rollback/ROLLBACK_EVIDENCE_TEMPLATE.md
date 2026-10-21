# Rollback evidence — complete with your actual test

> Do this on a separate test branch or a disposable copy of the repository. Never experiment on the only copy of your completed project.

## Purpose
Show that a tracked change can be safely undone using Git history.

## Test record
- Date/time:
- Test branch name:
- Baseline commit hash:
- Test commit hash:
- Revert commit hash:
- Result: [Pass/Fail]
- Notes:

## Safe example commands
```bash
git status
git switch -c rollback-demo
# Make a harmless change to a file, then:
git add README.md
git commit -m "Test rollback evidence"
git log --oneline -3
# Copy the test commit hash from the log, then revert that specific commit:
git revert <TEST_COMMIT_HASH>
git log --oneline -4
git status
```

If Git opens an editor, save and close it to finish the revert. If conflicts occur, stop and resolve them carefully; do not use destructive reset commands on your main branch.

## Evidence to attach
1. Screenshot of the test commit in Git history.
2. Screenshot of the revert commit in Git history.
3. Screenshot of `git status` after the revert.
4. Brief explanation of what changed and how the revert restored the previous state.

Replace every placeholder with your real results. Do not invent hashes or screenshots.
