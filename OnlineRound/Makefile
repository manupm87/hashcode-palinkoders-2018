.PHONY: run test init profile zip publish

run:
	python main.py

test:
	pytest

init:
	python3 -m venv python_env
	( \
       source python_env/bin/activate; \
       pip3 install -r requirements.txt; \
    )

profile:
	( \
		source python_env/bin/activate; \
		mkdir -p profile; \
		python -m cProfile -o "profile/profile.prof" main.py; \
		snakeviz profile/profile.prof;\
    )

zip:
	rm -f online-round-palinkoders.zip;
	zip -r online-round-palinkoders.zip ../OnlineRound -x "*python_env*" -x "*__pycache*" -x "*.idea*" -x "*.pytest_cache*"

publish:
	mkdir -p dist;
	rm -rf dist/*;
	cp -f output/{example,small,medium,big}.out dist/ || :;
	make zip;
	cp online-round-palinkoders.zip dist/;

build: test run publish