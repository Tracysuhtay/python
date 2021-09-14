from flask import Flask, Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route('/linen')
def linen():
    return render_template('linen.html')

@auth.route('/curtain')
def curtain():
    return render_template("curtain.html")

@auth.route('/uniform')
def uniform():
    return render_template('uniform.html')

@auth.route('/plastic')
def plastic():
    return render_template('plastic.html')

@auth.route('/cartonbox')
def carton_box():
    return render_template('carton_box.html')

@auth.route('/software')
def software():
    return render_template('software.html')

@auth.route('/advisory')
def advisory():
    return render_template('advisory.html')

@auth.route('/social')
def social():
    return render_template('social.html')

@auth.route('/about_us')
def about_us():
    return render_template('about_us.html')

@auth.route('/contact')
def contact():
    return render_template('contact.html')