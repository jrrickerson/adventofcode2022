# adventofcode2022
Advent of Code puzzles and solutions for 2022: https://adventofcode.com/2022

## Using this repository
This is my personal repository for Advent of Code solutions, but anyone is
welcome to use all or part of it to aid in their own solutions.  I have created
some automation to help me be lazy during the puzzle season, primarily using
GNU Make.

## Initial Setup - Python
* I use [pyenv](https://github.com/pyenv/pyenv) to manage my Python versions, and
have targeted Python 3.11 for this repo primarily because it's newer and I
wanted to try it out.
* I use [pipenv](https://pipenv.pypa.io/en/latest/) to manage Python
virtualenvs and install dependencies.  The Pipfile and Pipfile.lock files are
provided.  My primary dependencies are `pytest` and `coverage` for
TDD / testing workflow, and `jinja2-cli` for automatic creations of daily
solution files via templates.
* Because they are programming language agnostic, the puzzle text and input
data files for each day's puzzle are manually downloaded and copied into the
[puzzles](./puzzles) directory as plaintext files.  I may automate this later
if I'm not too lazy to figure out the authentication bit.  Note that AoC data
is generated randomly per indivdual user, so my data will not match yours.

### Make targets
The Python solutions utilize GNU Make to automate common daily setup and
testing tasks.

**Environment Variables**
The Makefile expects an environment variable named `DAY` to indicate which day's
puzzle to operate on.  This is used by most of the make targets. You can specify
the day per command, as in `DAY=1 make solve` or set it once via `export` to
reduce repetition, as follows:

```bash
$ export DAY=1
$ make setup
$ make test
$ make solve
```

`make setup` - Creates the "day" directory for the puzzle and uses the Jinja2
templates to create an initial skeleton script and support files.

`make edit` - Open the script files created by `setup` in the configured editor
(default: vim)

`make test` - Runs `pytest` on the current "day" directory

`make solve` - Execute the "solve.py" script in the current day's directory to
run the puzzle solution and provide an answer to paste into the AoC website.

`make timer` - Execute the "solve.py" script as in the `solve` target but using
instrumentation to provide feedback on optimizing puzzle solutions.

`make cover` - Runs [coverage](https://coverage.readthedocs.io/en/6.5.0/) while
executing `pytest` to provide feedback on unit test coverage.


## Other Languages
Any additional solutions in other languages will be found in root-level
subdirectories named for those languages.  README files within those
directories will document setup and execution steps.
