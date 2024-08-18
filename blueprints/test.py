from flask import Blueprint, render_template

bp = Blueprint("1", __name__, url_prefix="")


@bp.route("/模板.html")
def main_page():
    return render_template("模板.html")


@bp.route('/compound_new_data_.html')
def show_new():
    return render_template("compound_new_data_.html")


@bp.route('/compound_3_1.html')
def show_3_1():
    return render_template("compound_3_1.html")


@bp.route('/compound_4_2.html')
def show_4_2():
    return render_template("compound_4_2.html")


@bp.route('/compound_4_5.html')
def show_4_5():
    return render_template("compound_4_5.html")


@bp.route('/compound_7_1.html')
def show_7_1():
    return render_template("compound_7_1.html")


@bp.route('/compound_7_2.html')
def show_7_2():
    return render_template("compound_7_2.html")


@bp.route('/compound_7_liquid.html')
def show_7_liquid():
    return render_template("compound_7_liquid_.html")


@bp.route('/compound_8_0_gas_')
def show_8_0():
    return render_template("compound_8_0_gas_.html")


@bp.route('/compound_8_1.html')
def show_8_1():
    return render_template("compound_8_1.html")


@bp.route('/compound_9_0.html')
def show_9_0():
    return render_template("compound_9_0.html")


@bp.route('/compound_9_1.html')
def show_9_1():
    return render_template("compound_9_1.html")


@bp.route('/compound_9_2______.html')
def show_9_2():
    return render_template("compound_9_2______.html")


@bp.route('/compound_9_3.html')
def show_9_3():
    return render_template("compound_9_3.html")


@bp.route('/compound_11_0______.html')
def show_11_0():
    return render_template("compound_11_0______.html")


@bp.route('/compound_11_1______.html')
def show_11_1():
    return render_template("compound_11_1______.html")


@bp.route('/compound_13_0.html')
def show_13_0():
    return render_template("compound_13_0.html")


@bp.route('/compound_13_0_erase_.html')
def show_13_0_erase():
    return render_template("compound_13_0_erase_.html")


@bp.route('/compound_13_1_remove_.html')
def show_13_1():
    return render_template("compound_13_1_remove_.html")


@bp.route('/compound_13_2_clear_.html')
def show_13_2():
    return render_template("compound_13_2_clear_.html")


@bp.route('/compound_14_0.html')
def show_14_0():
    return render_template("compound_14_0.html")


@bp.route('/compound_14_1____.html')
def show_14_1():
    return render_template("compound_14_1____.html")


@bp.route('/compound_14_2_1.html')
def show_14_2_1():
    return render_template("compound_14_2_1.html")


@bp.route('/compound_14_3.html')
def show_14_3():
    return render_template("compound_14_3.html")


@bp.route('/compound_14_4_____.html')
def show_14_4():
    return render_template("compound_14_4_____.html")


@bp.route('/compound_14_5.html')
def show_14_5():
    return render_template("compound_14_5.html")


@bp.route('/compound_15_1.html')
def show_15_1():
    return render_template("compound_15_1.html")


@bp.route('/compound_15_2.html')
def show_15_2():
    return render_template("compound_15_2.html")


@bp.route('/compound_16_1.html')
def show_16_1():
    return render_template("compound_16_1.html")


@bp.route('/compound_17_1.html')
def show_17_1():
    return render_template("compound_17_1.html")


@bp.route('/compound__solid_.html')
def show_solid():
    return render_template("compound__solid_.html")


@bp.route('/登录页.html')
def show_login():
    return render_template("登录页.html")


@bp.route('/帮助信息主页.html')
def show_help():
    return render_template("帮助信息主页.html")


@bp.route('/resources/reload.html')
def show_re_main():
    return render_template("reload.html")
