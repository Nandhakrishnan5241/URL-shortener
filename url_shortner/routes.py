from flask import Blueprint, render_template, request, redirect

shortener = Blueprint('shortener',__name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    return ''

@shortener.route('/create_link',methods=['POST'])
def create_link():
    return ''

@shortener.route('/')
def index():
    return render_template('index.html')

@shortener.route('/analytics')
def analytics():
    return ''

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1>page not found 404</h1>',404