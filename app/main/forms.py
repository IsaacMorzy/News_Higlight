from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired,Required

class HeadlineForm(FlaskForm):
    pass

class LanguageForm(FlaskForm):
    language = SelectField("select_language",choices=[('en','en'),('ar','ar'),('de','de'),('es','es'),('fr','fr'),('he','he'),('it','it'),('nl','nl'),('no','no'),('ru','ru'),('se','se'),('ud','ud'),('zh','zh')],validators=[DataRequired()])
    submit = SubmitField('proceed')
