from flask import render_template, request, redirect, url_for
from app import db
from app.models import Server, Log
from app.ssh import SSHClient
from app.usn import USNParser
import datetime

def init_routes(app):
    @app.route("/")
    def index():
        servers = Server.query.all()
        return render_template("index.html", servers=servers)

    @app.route("/add_servers", methods=["POST"])
    def add_servers():
        file = request.files.get("server_file")
        if not file:
            return redirect(url_for("index"))

        for line in file.read().decode().splitlines():
            hostname, ip_address = line.split(",")
            existing = Server.query.filter_by(ip_address=ip_address).first()
            if not existing:
                server = Server(hostname=hostname, ip_address=ip_address)
                db.session.add(server)

        db.session.commit()
        return redirect(url_for("index"))

    @app.route("/logs")
    def logs():
        logs = Log.query.order_by(Log.timestamp.desc()).all()
        return render_template("logs.html", logs=logs)

    @app.route("/scan_server/<int:server_id>")
    def scan_server(server_id):
        server = Server.query.get_or_404(server_id)
        ssh = SSHClient(server.ip_address, "username", "password")  # Adjust as needed
        if ssh.connect():
            output, _ = ssh.execute_command("lsb_release -a")
            server.os_version = output.split("\n")[1].split(":")[1].strip() if output else "Unknown"
            ssh.close()

            log = Log(timestamp=datetime.datetime.now(), action="Scan", details="Scanned OS version.", server=server)
            db.session.add(log)
            db.session.commit()

        return redirect(url_for("index"))
