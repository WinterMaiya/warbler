from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField("text", validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])
    image_url = StringField("(Optional) Image URL")


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class EditProfileForm(FlaskForm):
    """Edit your profile form"""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    image_url = StringField("Profile Image URL")
    image_header_url = StringField("Image Header Url")
    bio = TextAreaField("Bio", validators=[Length(max=200)])
    location = StringField("Location", validators=[Length(max=50)])
    password = PasswordField("Password", validators=[Length(min=6)])
