from flask import Flask

app = Flask('app')


@app.route('/home')
def hello_world():
  return 'Hello, World! Ismail'


if __name__ == '__main__':
  app.run(debug=True)
#making a small change

#We are done with this version and we changed the file to python file
