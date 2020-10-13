from flask import Flask
from flask import render_template, abort
application = Flask(__name__)

@application.route('/100')
def return_100():
    return render_template('100.html'),100

@application.route('/')
def return_200():
    return 'Status Code:200'

@application.route('/201')
def return_201():
    return render_template('100.html'),201

@application.route('/202')
def return_202():
    return render_template('100.html'),202

@application.route('/203')
def return_203():
    return render_template('100.html'),203

@application.route('/204')
def return_204():
    return render_template('100.html'),204


@application.route('/205')
def return_205():
    return render_template('100.html'),205

@application.route('/206')
def return_206():
    return render_template('100.html'),206

@application.route('/300')
def return_300():
    return render_template('100.html'),300

@application.route('/301')
def return_301():
    return render_template('100.html'),301

@application.route('/302')
def return_302():
    return render_template('100.html'),302

@application.route('/303')
def return_303():
    return render_template('100.html'),303

@application.route('/304')
def return_304():
    return render_template('100.html'),304

@application.route('/305')
def return_305():
    return render_template('100.html'),305

@application.route('/307')
def return_307():
    return render_template('100.html'),307

@application.route('/308')
def return_308():
    return render_template('100.html'),308

@application.route('/400')
def return_400():
    return render_template('100.html'),400

@application.route('/401')
def return_401():
    return render_template('100.html'),401

@application.route('/402')
def return_402():
    return render_template('100.html'),402

@application.route('/403')
def return_403():
    return render_template('100.html'),403

@application.route('/404')
def return_404():
    return render_template('100.html'),404

@application.route('/405')
def return_405():
    return render_template('100.html'),405

@application.route('/406')
def return_406():
    return render_template('100.html'),406

@application.route('/407')
def return_407():
    return render_template('100.html'),407

@application.route('/408')
def return_408():
    return render_template('100.html'),408

@application.route('/409')
def return_409():
    return render_template('100.html'),409

@application.route('/410')
def return_410():
    return render_template('100.html'),410

@application.route('/411')
def return_411():
    return render_template('100.html'),411

@application.route('/412')
def return_412():
    return render_template('100.html'),412

@application.route('/413')
def return_413():
    return render_template('100.html'),413

@application.route('/414')
def return_414():
    return render_template('100.html'),414

@application.route('/415')
def return_415():
    return render_template('100.html'),415

@application.route('/500')
def return_500():
    return render_template('100.html'),500

@application.route('/501')
def return_501():
    return render_template('100.html'),501

@application.route('/502')
def return_502():
    return render_template('100.html'),502

@application.route('/503')
def return_503():
    return render_template('100.html'),503

@application.route('/504')
def return_504():
    return render_template('100.html'),504

@application.route('/505')
def return_505():
    return render_template('100.html'),505

if __name__ == '__main__':
    application.run(host='0.0.0.0')

