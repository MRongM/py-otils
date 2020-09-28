def start_flask(route='/',port=8064):    
    from flask import Flask 
    app = Flask('otil_server')
    aroute=app.route(route)
    import os,sys
    # model_path,model = os.path.split(file_path)
    def hello_world():
        return 'Hello World!'
    aroute(hello_world)
    # sys.path.insert(0,model_path)
    # module=__import__(model)
    # module.apply()
    app.run(host='0.0.0.0',port=port)    

if __name__ == '__main__':
    import sys
    
    start_flask()