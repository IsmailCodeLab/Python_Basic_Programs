from flask import Flask

app = Flask('app')


@app.route('/index')
def index():
  return 'This is index'


if __name__ == '__main__':
  app.run(debug=True)
#We are done with this version and we changed the file to python file
