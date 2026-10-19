Git and Commit Requirements

After completing the analysis:

1. Run the relevant repository validation and tests that are appropriate for the changes made.

2. Verify that the analysis deliverable is complete and that no prohibited files were modified.

3. Review the final diff and run "git diff --check".

4. Commit the new analysis report in a separate commit using the message:
   
   "analysis: document Decision ADR relationship"

5. The commit must contain only "engineering/analysis/architecture/Decision-ADR-Relationship-Analysis.md".

6. Do not include unrelated working-tree changes in the commit. Do not stage or commit files belonging to other tasks or user work.

7. Do not push any commits.

8. Report the commit hash, the committed file, the validation and test results, and the final working-tree status.

9. If the commit cannot be completed safely—for example, because unrelated changes prevent a clean and unambiguous commit—stop and report the exact reason instead of forcing the operation.
