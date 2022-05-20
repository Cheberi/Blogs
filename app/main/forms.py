from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[InputRequired()])
    post = TextAreaField("Type Away:", validators=[InputRequired()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[InputRequired()])
    post = TextAreaField("Type Away", validators=[InputRequired()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[InputRequired()])
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")