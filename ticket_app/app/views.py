from app import my_app
from flask import render_template
from flask import request
import sqlite3 as sql
from app.forms import FoodySearch
from app.forms import LazadaSearch
from app.forms import VatgiaSearch
from app.forms import TikiSearch
from app.forms import ThegioididongSearch
from app.forms import SendoSearch
from app.ticket_scraper_foody import get_post_foody
from app.ticket_scraper_lazada import get_post_lazada
from app.ticket_scraper_vatgia import get_post_vatgia
from app.ticket_scraper_tiki import get_post_tiki
from app.ticket_scraper_thegioididong import get_post_thegioididong
from app.ticket_scraper_sendo import get_post_sendo
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')
@my_app.route('/search_foody', methods=['GET', 'POST'])
def search_foody():
	posts = []
	form = FoodySearch()
	if form.validate_on_submit():
		event 		= form.foody_name.data
		location 	= form.location.data
		position 	= form.position.data
		posts 		= get_post_foody(event, position, location)
	return render_template('search_foody.html', title='Search for a Restaurant', form=form, posts=posts)
@my_app.route('/search_lazada', methods=['GET', 'POST'])
def search_lazada():
	posts = []
	form = LazadaSearch()
	if form.validate_on_submit():
		event	 		= form.lazada_name.data
		posts			= get_post_lazada(event)
	return render_template('search_lazada.html', title='Search for a Product', form=form, posts=posts)
@my_app.route('/search_vatgia', methods=['GET','POST'])
def search_vatgia():
	posts = []
	form = VatgiaSearch()
	if form.validate_on_submit():
		event	 		= form.vatgia_name.data
		posts			= get_post_vatgia(event)
	return render_template('search_vatgia.html', title='Search for a Product', form=form, posts=posts)
@my_app.route('/search_tiki', methods=['GET','POST'])
def search_tiki():
	posts = []
	form = TikiSearch()
	if form.validate_on_submit():
		event	 		= form.tiki_name.data
		posts			= get_post_tiki(event)
	return render_template('search_tiki.html', title='Search for a Product', form=form, posts=posts)
@my_app.route('/search_thegioididong', methods=['GET','POST'])
def search_thegioididong():
	posts = []
	form = ThegioididongSearch()
	if form.validate_on_submit():
		event	 		= form.thegioididong_name.data
		posts			= get_post_thegioididong(event)
	return render_template('search_thegioididong.html', title='Search for a Product', form=form, posts=posts)
@my_app.route('/search_sendo', methods=['GET','POST'])
def search_sendo():
	posts = []
	form = SendoSearch()
	if form.validate_on_submit():
		event	 		= form.sendo_name.data
		posts			= get_post_sendo(event)
	return render_template('search_sendo.html', title='Search for a Product', form=form, posts=posts)
@my_app.route('/history')
def history():
	return render_template('history.html')
@my_app.route('/feedback')
def feedback():
	return render_template('feedback.html')
@my_app.route('/admin')
def admin():
	return render_template('admin.html')
@my_app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name', value='values')
    return response
