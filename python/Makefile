# Day number left-padded to 2 digits
DAY_NAME = $(shell printf "%02g" $(DAY))
# Directory name for day code and data
DAY_DIR = day-$(DAY_NAME)
EDITOR=vim
RUNTIME=python3
TEST_RUNTIME="pytest -v"


# Create a new directory for solving a new day
setup:
	mkdir -p $(DAY_DIR)
	test ! -e "$(DAY_DIR)/solve.py" && \
		jinja2 solve.py.j2 -D DAY=$(DAY) -D URL="$(URL)" > $(DAY_DIR)/solve.py

# Open solution script in editor
edit:
	$(EDITOR) $(DAY_DIR)/solve.py

# Run solution for specific day
solve:
	$(RUNTIME) $(DAY_DIR)/solve.py

# Run solution for specific level with instrumentation
timer:
	@time -f "Execution time: %es" $(RUNTIME) $(DAY_DIR)/solve.py

# Run Pytest on the current day
test:
	$(TEST_RUNTIME) $(DAY_DIR)
