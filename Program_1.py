from flask import Flask

app = Flask('app')


@app.route('/home')
def hello_world():
  return 'Hello, World! This is Ismail'
  
@app.route('/about')
def about():
  return jsonify({'name':'Shaik Ismail'})


if __name__ == '__main__':
  app.run(debug=True)
#making a small change
