from flask import Flask, render_template,flash,redirect,url_for
app = Flask(__name__)
app.secret_key = 'wertyuiop2345'

user={
    'name':'Jeff Zhang'
    ,'bio':'He is a man'
    }
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

app.jinja_environment.trim_blocks = True
app.jinja_environment.lstrip_blocks = True

#自定义上下文
app.context_processor(lambda : dict(foo = 'Jeff is foo'))
#等价方法1（装饰器）
#@app.context_processor
#def foo():
#    foo = 'Jeff is foo'
#    return dict(foo=foo)

#等价方法2（作为方法调用）
#def foo():
#    foo = 'Jeff is foo'
#    return dice(foo)
#app.context_processor(foo)
   
#自定义全局函数
@app.template_global()
def bar():
    return 'I am abaaba'

#自定义过滤器
@app.template_filter()
def smile(s):
    return s + ' :)'

@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False



@app.route('/flash')
def just_flash():
    flash('I am flash , what\'s up bro?')
    return redirect(url_for('index'))


@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html',user=user,movies=movies)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404