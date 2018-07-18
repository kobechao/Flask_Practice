from app_blog import app
from app_blog import db
from flask import render_template
from app_blog.author.model import UserRegister
from app_blog.author.form import FormRegister 

@app.route('/register', methods=['GET', 'POST'] )
def register() :
	
	form = FormRegister()
	
	if form.validate_on_submit() :
		user = UserRegister(
			username = form.username.data,
			email = form.email.data,
			password = form.password.data,
		)

		db.session.add( user )
		db.session.commit()
		return "Success"

	return render_template( 'author/register.html', form=form )


if __name__ == '__main__':
	app.run( port=8000, debug=True )