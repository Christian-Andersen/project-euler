# Define the executable name
SOURCE_FILE = 1.c
OUTPUT_FILE = a.out

# Phony targets don't create files, they are just names for commands.
.PHONY: all run clean

# The default target that performs the entire sequence: build, run, and clean.
# This target ensures each step happens in order.
all: $(OUTPUT_FILE) run clean

# This is the primary build rule. It states that the 'a.out' executable depends
# on the source file. If the source file is newer than the executable,
# the `gcc` command will be run to rebuild it.
$(OUTPUT_FILE): $(SOURCE_FILE)
	gcc $(SOURCE_FILE) -o $(OUTPUT_FILE)

# This target runs the executable. It depends on the `a.out` file existing.
run: $(OUTPUT_FILE)
	./$(OUTPUT_FILE)

# This target removes the executable file. It's a standard practice
# for cleaning up the project.
clean:
	rm $(OUTPUT_FILE)

