git pull
../venv/bin/activate
pip -r install requirements/base.txt
systemctl restart smarthouse
systemctl restart nginx 