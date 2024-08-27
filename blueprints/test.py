from flask import Blueprint, render_template

bp = Blueprint("1", __name__, url_prefix="/test")


@bp.route("/1")
def test():
    return render_template("compound_11_0______.html")
