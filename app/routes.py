from flask import render_template, request, redirect, url_for
from app import db
from app.models import Server, Log
from app.ssh_utils import check_server_version, update_server_packages
from app.usn_utils import fetch_usn_data
import os

def init_routes(app):
    @app.route('/')
    def index():
        servers = Server.query.all()
        return render_template('index.html', servers=servers)

    @app.route('/add_servers', methods=['POST'])
    def add_servers():
        file = request.files['server_file']
        if file:
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            add_servers_from_file(filepath)
        return redirect(url_for('index'))

    @app.route('/scan_server/<int:server_id>')
    def scan_server(server_id):
        server = Server.query.get(server_id)
        if server:
            os_version, installed_packages = check_server_version(server.ip_address)
            usn_data = fetch_usn_data()
            updates_needed = compare_updates(os_version, installed_packages, usn_data)
            return render_template('server_list.html', server=server, updates_needed=updates_needed)
        return redirect(url_for('index'))

    @app.route('/update_server/<int:server_id>')
    def update_server(server_id):
        server = Server.query.get(server_id)
        if server:
            success = update_server_packages(server.ip_address)
            log_action(server, 'Update', 'Packages updated successfully' if success else 'Update failed')
        return redirect(url_for('index'))

    @app.route('/logs')
    def logs():
        logs = Log.query.all()
        return render_template('logs.html', logs=logs)

def log_action(server, action, details):
    log = Log(action=action, details=details, server=server)
    db.session.add(log)
    db.session.commit()

def add_servers_from_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            ip_address, hostname = line.strip().split(',')
            if not Server.query.filter_by(ip_address=ip_address).first():
                new_server = Server(ip_address=ip_address, hostname=hostname)
                db.session.add(new_server)
    db.session.commit()
