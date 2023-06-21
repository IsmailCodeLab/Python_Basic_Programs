from flask import Flask

app = Flask('app')



@app.route('/home')
def hello_world():
  return 'Hello, World! This is Ismail'
  
@app.route('/about')
def about():
  return jsonify({'name':'Shaik Ismail'})

@app.route('/index')
def index():
  return 'This is index'



if __name__ == '__main__':
  app.run(debug=True)
  
#making a small change
#We are done with this version and we changed the file to python file
#Change after merging main and Flask_Apllication branches
