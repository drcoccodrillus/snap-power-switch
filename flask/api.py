#!/usr/bin/env python
from flask import Flask, jsonify
import subprocess


app = Flask(__name__)

@app.route('/reboot', methods=['GET'])
def reboot():
    try:
        subprocess.run(['dbus-send --system --print-reply \
        --dest=org.freedesktop.login1 /org/freedesktop/login1 \
        "org.freedesktop.login1.Manager.Reboot" boolean:true'], shell=True)
        return jsonify(status='OK', message='Machine is rebooting')
    except subprocess.CalledProcessError:
        return jsonify(status='KO', message='Reboot command failed')

@app.route('/suspend', methods=['GET'])
def suspend():
    try:
        subprocess.run(['dbus-send --system --print-reply \
        --dest=org.freedesktop.login1 /org/freedesktop/login1 \
        "org.freedesktop.login1.Manager.Suspend" boolean:true'], shell=True)
        return jsonify(status='OK', message='Machine is suspending')
    except subprocess.CalledProcessError:
        return jsonify(status='KO', message='Suspend command failed')

@app.route('/hibernate', methods=['GET'])
def hibernate():
    try:
        subprocess.run(['dbus-send --system --print-reply \
        --dest=org.freedesktop.login1 /org/freedesktop/login1 \
        "org.freedesktop.login1.Manager.Hibernate" boolean:true'], shell=True)
        return jsonify(status='OK', message='Machine is hibernating')
    except subprocess.CalledProcessError:
        return jsonify(status='KO', message='Hibernate command failed')

@app.route('/poweroff', methods=['GET'])
def poweroff():
    try:
        subprocess.run(['dbus-send --system --print-reply \
        --dest=org.freedesktop.login1 /org/freedesktop/login1 \
        "org.freedesktop.login1.Manager.PowerOff" boolean:true'], shell=True)
        return jsonify(status='OK', message='Machine is shutting down')
    except subprocess.CalledProcessError:
        return jsonify(status='KO', message='Shutdown command failed')


def main():
    app.run()


if __name__ == '__main__':
    app.run()
