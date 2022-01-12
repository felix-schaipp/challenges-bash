# Challenge 2: Web app - URL shorting

## Description

---

Your assignment is to implement a URL shortening service using Python (backend) and any framework.

## Required functionality

---

short link is a URL shortening service where you enter a URL such as `https://en.wikipedia.org/wiki` Computer and it returns a short URL such as `http://short.est/GeAi9K`.

## Requirements

---

There is no restriction on how your encode/decode algorithm should work. You just need to make sure that a URL can be encoded to a short URL and the short URL can be decoded to the original URL. Please follow these requirements:

- Language: **Python**
- Framework: **any framework**
- Two endpoints are required
  - **/encode** - Encodes a URL to a shortened URL
  - **/decode** - Decodes a shortened URL to its original URL.
- Both endpoints should **return JSON**
- **Provide API tests** for both endpoints
- **Display a web UI** to de- and encode short URLs
- **Provide detailed instructions** on how to run your assignment in a separate markdown file
- You do not need to persist short URLs to a database. Keep them in memory.
- **Bonus**: Store all shortened URLs in a simple database (e.g. mongoDB)

### Evaluation Criteria

---

- **Best Practice: Python** best practices
- **API:** API implemented featuring a /encode and /decode endpoint
- **Completeness:** did you complete the features? Are all the tests running?
- **Correctness:** does the functionality act insensible, thought-out ways?
- **Maintainability:** is it written in a clean, maintainable way?
- **Auditability:** Show us your work through your commit history

## How to start

---

- install the dependencies with `make deps-install`
- export env variables:
  - `export FLASK_SECRET=902h349r0p78w2q34ddqwere`
  - `export FLASK_APP=app`
  - `export FLASK_ENV=development`
- initialize the sqllite database with `python3 initializeDb.py`
- run

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

- [x] boilerplate setup
- [ ] create sqllite schema
- [ ] create index page for input
- [ ] encode/decode routes
- [ ] tests
