.PHONY: migrate bootstrap validate test build clean tree

migrate:
	python tools/migrate_v2_shared_artwork.py

bootstrap:
	python tools/bootstrap_artwork.py

validate:
	python tools/validate_addons.py
	python tools/secret_scan.py
	python -m compileall -q addons tools tests

test:
	python -m unittest discover -s tests -p "test_*.py" -v

build: bootstrap validate test
	python tools/build_repo.py

clean:
	python tools/clean_build.py

tree:
	python tools/print_tree.py
