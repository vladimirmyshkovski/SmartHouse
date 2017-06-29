git pull
. /var/www/venv/bin/activate
pip install -r requirements/base.txt
systemctl restart smarthouse
systemctl restart nginx 