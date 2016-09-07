from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from werkzeug.routing import BaseConverter
from werkzeug import secure_filename
from flask.ext.script import Manager

from os import path



app = Flask(__name__)

manager=Manager(app)

@app.route('/')
def index():
	response=make_response(render_template('index.html',title='Welcome'))
	response.set_cookie('username','')
	return render_template('index.html',title='Welcome')
	
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
	if request.method=='POST':
		#post情况下，获取用户名和密码
		username=request.form['username']
		password=request.form['password']
	else: 
		#get 的情况下
		username=request.args['username']
	return render_template('login.html',method=request.method)

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
	app.run(debug=True)
	manager.run()
	


