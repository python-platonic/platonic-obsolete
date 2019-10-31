venv:
	virtualenv -p /usr/bin/python3.7 venv


develop:
	venv/bin/pip install -e .[dev]
