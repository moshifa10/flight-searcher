#!/bin/bash

echo "Hello I am Njabs"
echo "I will be running it using shell"

git add data_manager.py main.py requirements.txt flight_search.py flight_data.py exchange_rate.py notification_manager.py test.sh
git commit -m "Done: intergrated with google forms to accept users if they want to be in the programme"
git push origin main
