# Day number left-padded to 2 digits
DAY_NAME = $(shell printf "%02g" $(DAY))
# Directory name for day code and data
DAY_DIR = day-$(DAY_NAME)
EDITOR?=vim
EDITOR_OPTIONS=-p
RUNTIME?=python3


# Create a new directory for solving a new day
setup:
	mkdir -p $(DAY_DIR)
	test ! -e "$(DAY_DIR)/solve.py" && \
		jinja2 solve.py.j2 -D DAY=$(DAY) -D DAY_NAME="$(DAY_NAME)" > $(DAY_DIR)/solve.py
	touch "$(DAY_DIR)/utils.py"
	touch "$(DAY_DIR)/test_solve.py"
	touch "../puzzles/day-$(DAY_NAME).txt"
	touch "../puzzles/day-$(DAY_NAME).input"

# Open solution script in editor
edit:
	$(EDITOR) $(EDITOR_OPTIONS) $(DAY_DIR)/solve.py $(DAY_DIR)/utils.py $(DAY_DIR)/test_solve.py

# Run solution for specific day
solve:
	$(RUNTIME) $(DAY_DIR)/solve.py

# Run solution for specific level with instrumentation
timer:
	@time -f "Execution time: %es" $(RUNTIME) $(DAY_DIR)/solve.py

# Run Pytest on the current day
test:
	pytest $(DAY_DIR)

# Run coverage and get a report on the current day
cover:
	coverage run -m pytest $(DAY_DIR) && coverage report
