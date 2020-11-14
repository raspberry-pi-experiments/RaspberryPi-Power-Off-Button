install:
	@mkdir -p ~/.local/bin
	@cp poweroff.py ~/.local/bin
	@sudo cp poweroff.service /etc/systemd/system
	@sudo systemctl enable poweroff.service
	@sudo systemctl start poweroff.service
	@systemctl status poweroff.service


uninstall:
	@sudo systemctl stop poweroff.service
	@sudo systemctl disable poweroff.service
	@sudo rm -rf /etc/systemd/system/poweroff.service
	@rm -rf .local/bin/poweroff.py
