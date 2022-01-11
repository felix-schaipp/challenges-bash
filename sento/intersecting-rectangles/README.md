# Challenge 1 - intersecting rectangles

## Description

---

You have a JSON that contains the coordinates of two rectangles. Using the JSON as input, you should determine whether any specified rectangles intersect or not.

### Evaluation Criteria

---

- **Best practice:** Use best practices of your chosen language
- **Auditability:** Show us how you work through your commit history
- **Completeness:** did you complete the features? Are all the unit tests running?
- **Correctness:** does the functionality act insensible, thought-out ways?
- **Maintainability:** is it written in a clean, maintainable way?

## How to start

To test the challenge `make run` and `make test`
Boilerplate python project copied from [Alexander Willner](https://github.com/AlexanderWillner/python-boilerplate)

```bash
$ make [command]

available commands:
 * run          - Run the code.
 * test         - Run unit tests and test coverage.
 * doc          - Document code (pydoc).
 * clean        - Cleanup (e.g. pyc files).
 * code-style   - Check code style (pycodestyle).
 * code-lint    - Check code lints (pyflakes, pyline).
 * code-count   - Count code lines (cloc).
 * deps-install - Install dependencies (see requirements.txt).
 * deps-update  - Update dependencies (via pur).
```

### Plan

- [ ] write a small class and function to generate random rectangles to json
- [ ] test the random rectangles generator
- [ ] write a small class to import the pairs of rectangles and check for intersection
- [ ] test the class
- [ ] invite `nimarb` to the project for review
