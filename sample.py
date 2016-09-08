# -*- coding:utf-8 -*-
from flask import Flask,render_template,request,flash,redirect,url_for,make_response,abort
from werkzeug.routing import BaseConverter
from werkzeug import secure_filename
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

from os import path

nav=Nav()

app = Flask(__name__)
Bootstrap(app)

app.config.from_pyfile('config')
manager=Manager(app)

nav.register_element('top',Navbar(u'Flask入门',
								   View(u'主页','index'),
								   View(u'关于','about'),
								   View(u'服务','services'),
								   View(u'项目','projects')
								   ))

nav.init_app(app)
   
@app.route('/')
def index():
	response=make_response(render_template('index.html',title='Welcome'))
	response.set_cookie('username','te')
	return response
	
@app.route('/services')
def services():
	return 'Service'
	
@app.route('/about')
def about():
	return 'about'
	
@app.route('/projects/')
@app.route('/our-works/')
def projects():
	return 'The projects page'
	
@app.route('/login',methods=['GET','POST'])
def login():
	from forms import LoginForm
	form=LoginForm()
	flash(u'登录成功')
	return render_template('login.html',title=u'登录',form=form)

#上传文件
@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		f=request.files['file']
		basepath=path.abspath(path.dirname(__file__))
		#upload_path=path.join(basepath,'static\\uploads')
		up_file=secure_filename(f.filename)
		#                     存储地址             存储文件
		f.save(path.join(basepath,'static/uploads',up_file))
		return redirect(url_for('upload'))
	return render_template('upload.html')
	
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404
	
@app.template_test("current_link")
def is_current_link(link):
	return link==request.path
	
	
@manager.command
def dev():
	from livereload import Server
	live_server=Server(app.wsgi_app)
	live_server.watch('**/*.*')
	live_server.serve(open_url=True)
	

if __name__=='__main__':
	dev  #自动更新
	app.run(debug=True)
	
	


