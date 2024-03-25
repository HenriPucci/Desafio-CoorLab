#!/bin/bash

# Start the Python backend
python3 app.py &

# Store the PID of the Python process
PYTHON_PID=$!

# Start the Vue.js frontend
cd cb_viagens_app
yarn serve

# Once the frontend server is stopped, kill the Python process
kill $PYTHON_PID

echo "Implemente aqui o script para executar a sua solução"
