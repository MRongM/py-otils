def start_flask(file_path,port=8064):    
    import os,sys,json
    from flask import Flask,request,jsonify

    app = Flask('otil_server')

    @app.route('/',methods=['POST'])
    def handle():
        data = request.get_data()
        input_data = json.loads(data.decode('utf-8'))

        model_path,py_file = os.path.split(file_path)
        model = py_file.split('.py')[0]
        sys.path.insert(0,model_path)
        module = __import__(model)
        result = module.apply(input_data)
        return jsonify(result), 200

    app.run(host='0.0.0.0',port=port)    

if __name__ == '__main__':
    import sys
    print('sys.argv:',sys.argv)
    _,port,file_path = sys.argv
    start_flask(file_path,int(port))