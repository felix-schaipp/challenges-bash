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

To test the challenge install the dependencies with `make deps-install` and then `make run` and `make test`.
Expect tests to run.
You will be asked in the terminal (stdin) how many random pairs you wanna generate, this will output the pairs to json. These pairs will than be analysed and the output is printed to stdout.
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

- [x] build a small data structure for the rectangles to be stored
- [x] write small classes to generate random rectangles to json
- [x] test the random rectangles generator
- [x] write a small class to import the pairs of rectangles and check for intersection
- [x] test the class

### Possible improvements

To make it graphically more pleasing we could render each pair with numpy onto a canvas and than show if we have an intersection or not.
