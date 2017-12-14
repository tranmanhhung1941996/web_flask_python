from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
class FoodySearch(FlaskForm):
	foody_name = StringField('foody_name', validators=[DataRequired()])
	position = StringField('position', validators=[DataRequired()])
	location = SelectField('location', choices=[('Ha Noi', u'Ha Noi'), 
						('Sai Gon', u'Sai Gon'),
						('Hai Phong', u'Hai Phong'),
						('Da Nang', u'Da Nang'),
						('TP Hue', u'TP Hue'),
						('Nam dinh', u'Nam Dinh'),
						('Nha trang', u'Nha Trang'),
						('Can Tho', u'Can Tho'),
						('Da Lat', u'Da Lat')])
class LazadaSearch(FlaskForm):
	lazada_name = StringField('lazada_name', validators=[DataRequired()])
class VatgiaSearch(FlaskForm):
	vatgia_name = StringField('vatgia_name', validators=[DataRequired()])
class TikiSearch(FlaskForm):
	tiki_name = StringField('tiki_name', validators=[DataRequired()])
class ThegioididongSearch(FlaskForm):
	thegioididong_name = StringField('thegioididong_name', validators=[DataRequired()])
class SendoSearch(FlaskForm):
	sendo_name = StringField('sendo_name', validators=[DataRequired()])


