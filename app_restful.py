import io
import json
from flask import Flask, request, render_template, make_response, redirect, flash, url_for, send_file
from flask_restful import Resource, Api
from PIL import Image
import base64

app = Flask(__name__)
api = Api(app)


class MainPage(Resource):
    def get(self):
        return make_response(render_template('main.html'))
    
    def post(self):
        # if 'image' not in request.files:
        #     flash('No file part')
        #     return make_response(render_template('main.html'))
        
        im_content = io.BytesIO()
        im = Image.open(request.files['image'])
        im.save(im_content, format='png')
        im.show()
        im_content.seek(0)
        im_content = im_content.read()
        im_content = base64.b64encode(im_content)
        
        return redirect(url_for('crop', im_content=im_content))
    
    
class CropPage(Resource):
    def get(self):
        return make_response(render_template('crop.html', image=request.args.get('im_content')))

    
api.add_resource(MainPage, '/')
api.add_resource(CropPage, '/crop', endpoint='crop' )

if __name__ == '__main__':
    app.run(debug=True, port=5001)