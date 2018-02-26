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
		python -m cProfile -o "profile/profile.prof" main.py; \
		snakeviz profile/profile.prof;\
    )

zip:
	rm test-round-palinkoders.zip;
	zip -r test-round-palinkoders.zip ../TestRound -x "*python_env*" -x "*__pycache*" -x "*.idea*" -x "*.pytest_cache*"