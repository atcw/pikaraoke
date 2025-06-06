import json
import logging
import flask_babel
from flask import Blueprint, flash, redirect, render_template, request, url_for

from pikaraoke.lib.current_app import (
    broadcast_event,
    get_karaoke_instance,
    get_site_name,
    is_admin,
)

hold_bp = Blueprint("hold", __name__)

@hold_bp.route("/hold/continue", methods=["GET","POST"])
def hold_continue():
    k = get_karaoke_instance()
    #k.hold_dohold = False
    k.hold_do_continue = True
    k.update_now_playing_hash()
    broadcast_event("hold_continue")
    logging.info("hold_do_continue == true")
    return "continueing"
