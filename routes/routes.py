from flask import render_template, abort, make_response, redirect, url_for
from flask import request, Response

bookmarks = []

def store_bookmark(url):
    bookmarks.append( {'url':url })

def define_routes(application):

    @application.route('/add',methods=['GET','POST'])
    def add():
        if request.method == 'POST':
            url = request.form['url']
            store_bookmark(url)
            application.logger.debug('URL:' + url )
            return redirect(url_for('return_200'))
        return render_template('add.html')

    @application.route('/100')
    def return_100():
        print_request_info()
        return render_template('empty.html'),100

    @application.route('/')
    def return_200():
        print_request_info()
        content = render_template('index.html')
        application.logger.debug('content:' + content) 
        return make_response(content,200)

    @application.route('/201')
    def return_201():
        print_request_info()
        return render_template('empty.html'),201

    @application.route('/202')
    def return_202():
        print_request_info()
        return render_template('empty.html'),202

    @application.route('/203')
    def return_203():
        print_request_info()
        return render_template('empty.html'),203

    @application.route('/204')
    def return_204():
        print_request_info()
        return render_template('empty.html'),204

    @application.route('/205')
    def return_205():
        print_request_info()
        return render_template('empty.html'),205

    @application.route('/206')
    def return_206():
        print_request_info()
        return render_template('empty.html'),206

    @application.route('/300')
    def return_300():
        print_request_info()
        return render_template('empty.html'),300

    @application.route('/301')
    def return_301():
        print_request_info()
        return redirect(url_for('return_200'),301)

    @application.route('/302')
    def return_302():
        print_request_info()
        return redirect(url_for('return_200'),302)

    @application.route('/303')
    def return_303():
        print_request_info()
        return redirect(url_for('return_200'),303)

    @application.route('/304')
    def return_304():
        print_request_info()
        return render_template('empty.html'),304

    @application.route('/305')
    def return_305():
        print_request_info()
        return redirect(url_for('return_200'),305)

    @application.route('/307')
    def return_307():
        print_request_info()
        return redirect(url_for('return_200'),307)

    @application.route('/308')
    def return_308():
        print_request_info()
        return redirect(url_for('return_200'),308)

    @application.route('/400')
    def return_400():
        print_request_info()
        abort(400)

    @application.route('/401')
    def return_401():
        print_request_info()
        abort(401)

    @application.route('/402')
    def return_402():
        print_request_info()
        abort(402)

    @application.route('/403')
    def return_403():
        print_request_info()
        abort(403)

    @application.route('/404')
    def return_404():
        print_request_info()
        abort(404)

    @application.route('/405')
    def return_405():
        print_request_info()
        abort(405)

    @application.route('/406')
    def return_406():
        print_request_info()
        abort(406)

    @application.route('/407')
    def return_407():
        print_request_info()
        abort(407)

    @application.route('/408')
    def return_408():
        print_request_info()
        abort(408)

    @application.route('/409')
    def return_409():
        print_request_info()
        abort(409)

    @application.route('/410')
    def return_410():
        print_request_info()
        abort(410)

    @application.route('/411')
    def return_411():
        print_request_info()
        abort(411) 

    @application.route('/412')
    def return_412():
        print_request_info()
        abort(412)

    @application.route('/413')
    def return_413():
        print_request_info()
        abort(413)

    @application.route('/414')
    def return_414():
        print_request_info()
        abort(414)

    @application.route('/415')
    def return_415():
        print_request_info()
        abort(415)

    @application.route('/500')
    def return_500():
        print_request_info()
        abort(500)

    @application.route('/501')
    def return_501():
        print_request_info()
        abort(501)

    @application.route('/502')
    def return_502():
        print_request_info()
        abort(502)

    @application.route('/503')
    def return_503():
        print_request_info()
        abort(503)

    @application.route('/504')
    def return_504():
        print_request_info()
        abort(504)

    @application.route('/505')
    def return_505():
        print_request_info()
        abort(505)

    def print_request_info():
        print(request.headers)

    @application.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'),404

