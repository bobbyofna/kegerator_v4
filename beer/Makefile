SHELL:=/bin/bash

start:		restart

restart:	reload

reload:
		sudo systemctl restart uwsgi.service
		sudo systemctl daemon-reload

clean:
		sudo rm -rf /home/pi/kegerator/beer/*.py~
		sudo rm -rf /home/pi/kegerator/beer/*.pyc
		sudo rm -rf /home/pi/kegerator/*~
		sudo rm -rf /home/pi/kegerator/*.*~
