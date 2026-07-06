.PHONY: bootstrap validate test build clean tree

bootstrap:
	python tools/bootstrap_artwork.py

validate:
	python tools/validate_addons.py
	python tools/secret_scan.py
	python -m compileall -q addons tools tests

# Uses unittest so the base repository has no mandatory third-party dependency.
test:
	python -m unittest discover -s tests -p "test_*.py" -v

build: bootstrap validate test
	python tools/build_repo.py

clean:
	python tools/clean_build.py

tree:
	python tools/print_tree.py
