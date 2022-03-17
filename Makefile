VENV_DIR=venv
API_KEY ?= $(shell bash -c 'read -p "Openweather API Key: " pwd; echo $$pwd')

install:
	@if [ -d $(VENV_DIR) ]; then \
		echo "Dependecies already installed in $(VENV_DIR)."; \
	 else \
	 	echo "Installing in $(VENV_DIR)"; \
<<<<<<< HEAD
	 	python3 -m venv $(VENV_DIR); \
	 	. $(VENV_DIR)/bin/activate && pip3 install -r requirements_dev.txt && cd activity_suggestions && touch api_key.py && echo API_KEY = \"$(API_KEY)\" > api_key.py && cp .flaskenv.example .flaskenv; \
		cd ../react_frontend && npm install; \
=======
	 	sudo apt install python3.9 python3-pip -y && python3 -m venv $(VENV_DIR); \
	 	. $(VENV_DIR)/bin/activate && pip3 install -r requirements_dev.txt && cd activity_suggestions && touch api_key.py && echo API_KEY = \"$(API_KEY)\" > api_key.py && cp .flaskenv.example .flaskenv; \
		cd ../react_frontend && sudo apt install nodejs npm -y && npm install; \
>>>>>>> 1edf5dd6ac1baffd211ecb24133f5af7604ca6d4
	fi

start:
	@if [ -d $(VENV_DIR) ]; then \
		export PYTHONPATH="$${PWD}"; \
		. $(VENV_DIR)/bin/activate && cd activity_suggestions && flask run & \
		cd react_frontend && npm start & \
	else \
		echo "Execute make install first"; \
	fi

stop:
	@lsof -i :5000 | grep "5000" | awk '{print $$2}' | xargs -r kill -9
	@lsof -i :3000 | grep "3000" | awk '{print $$2}' | xargs -r kill -9
	@clear
