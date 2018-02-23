run:
	python3 main.py

test:
	pytest

init:
	pip3 install --user virtualenv
	virtualenv --python python3 python_env
	( \
       source python_env/bin/activate; \
       pip3 install -r requirements.txt; \
    )
