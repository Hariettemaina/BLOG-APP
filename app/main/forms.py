from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField, SelectField
from wtforms.validators import IputRequired

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[IputRequired()])
    post = TextAreaField("Type Away:", validators=[IputRequired()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[IputRequired()])
    post = TextAreaField("Type Away", validators=[IputRequired()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[IputRequired()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")