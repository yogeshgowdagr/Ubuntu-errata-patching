from app import db
from datetime import datetime

# Server model to store server details
class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(120), nullable=False)
    ip_address = db.Column(db.String(120), unique=True, nullable=False)
    os_version = db.Column(db.String(50))
    status = db.Column(db.String(20), default='active')
    last_checked = db.Column(db.DateTime, default=datetime.utcnow)
    last_error = db.Column(db.String(200))

# Log model to store execution logs
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'), nullable=False)
    action = db.Column(db.String(200))
    details = db.Column(db.Text)

    server = db.relationship('Server', back_populates="logs")

Server.logs = db.relationship('Log', back_populates="server", lazy=True)
