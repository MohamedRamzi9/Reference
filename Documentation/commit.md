### Commit messages format

<id>
Added:
- <description of added features with file paths>
Fixed:
- <description of fixed issues with file paths>
Changed:
- <description of changed features with file paths>
Removed:
- <description of removed features with file paths>
Refactored:
- <description of refactored features with file paths>

### Id
- A unique identifier, can be sequential number or timestamp, to reference the commit in the changelog. In my case, I use `C` followed by a sequential number, e.g., `C1`, `C2`, etc.

### File paths
- file paths should be relative to the project root for clarity.
- the format should be `path/to/file.ext` or `path/to/directory/` for directories.
- the file path should come last in the description of each change like so: - Added function `new_function` to `path/to/file.py`