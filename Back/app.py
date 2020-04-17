from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid
import json

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/login', methods=['GET', 'POST'])
def all_user():
    response_object = {'status': 'success'}
    if request.method == 'post':
        post_data = request.get_json()
        USER.append({
            'id': uuid.uuid4().hex,
            'Username': post_data.get('Username'),
            'Password': post_data.get('Password'),
        })
    else:
        return jsonify('Error!!!')
    return jsonify(response_object)

#@app.route('/login', methods=['POST'])
#def all_user():
#    response_object = {'status': 'success'}
#    if request.method == 'post':
#        post_data = request.get_json()
#        for user in USERS:
#            if user['Username'] == post_data.get('Username'):
#                response_object['message'] = True
#            else:
#                response_object['message'] = False
#    return jsonify(response_object)

@app.route('/neworder', methods=['POST'])
def addWares():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        WARES.append({
            'id': uuid.uuid4().hex,
            'Title': post_data.get('Title'),
            'Origin': post_data.get('Origin'),
            'Destination': post_data.get('Destination'),
            'Url': post_data.get('Url'),
            'Value': post_data.get('Value'),
            'Description': post_data.get('Description'),
            'Date': post_data.get('Date'),
            'Accept': post_data.get('Accept'),
            'imagePath': post_data.get('imagePath'),
        })
    return jsonify(response_object)

@app.route('/uploadimage', methods=['POST'])
def uploadimage():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        #Data = request.get_json()
        Data = request.form.get('formData')
        #upload = Data.get('formData')
        #filename = f'{uuid.uuid1()}_{secure_filename(upload.file.data.filename)}'
        #upload.file.data.save(f'static/uploads/{filename}')
        print(Data)
        response_object['filename'] = 'filename'
    return jsonify(response_object)

@app.route('/allorder', methods=['GET'])
def allorder():
    response_object = {'status': 'success'}
    response_object['wares'] = WARES
    return jsonify(response_object)

@app.route('/myorder', methods=['GET'])
def myorder():
    response_object = {'status': 'success'}
    response_object['wares'] = MYWARES
    return jsonify(response_object)

@app.route('/orderdetails/<ware_id>', methods=['GET', 'POST'])
def orderdetails(ware_id):
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        for ware in WARES:
            if ware['id'] == ware_id:
                MYWARES.append(ware)
    else:
        for ware in WARES:
            if ware['id'] == ware_id:
                response_object['ware'] = ware
    return jsonify(response_object)

@app.route('/myorderdetails/<ware_id>', methods=['GET'])
def myorderdetails(ware_id):
    response_object = {'status': 'success'}
    for ware in MYWARES:
        if ware['id'] == ware_id:
            response_object['ware'] = ware
    return jsonify(response_object)

@app.route('/myorderdetails/<ware_id>', methods=['DELETE'])
def myorderdelete(ware_id):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        removeOrder(ware_id)
    return jsonify(response_object)

def removeOrder(ware_id):
    for ware in MYWARES:
        if ware['id'] == ware_id:
            MYWARES.remove(ware)
            return True
    return False

@app.route('/acceptOrder/<ware_id>', methods=['GET','POST'])
def acceptOrder(ware_id):
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        for ware in WARES:
            if ware['id'] == ware_id:
                ware['comments'].append({
                    'name' : 'soheil75',
                    'rate' : 4 ,
                    'text' : post_data.get('text'),
                    'date' : post_data.get('date'),
                    'cost' : post_data.get('cost'),
                })
                MYWARES.append(ware)
    else:
        for ware in WARES:
            if ware['id'] == ware_id:
                response_object['ware'] = ware
    return jsonify(response_object)

WARES = [
    {
        'id': uuid.uuid4().hex,
        'imagePath':'141.jpg',
        'Title': 'توپ بسکتبال مولتن مدل GL7X',
        'Origin': 'آلمان',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'Accept':False,
        'username':'soheil75',
        'comments':[
            {
                'name':'transporter',
                'rate':4,
                'date':'1/1/2020',
                'cost':100,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
            {
                'name':'transporter88',
                'rate':1,
                'date':'1/7/2020',
                'cost':150,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
        ],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': True
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': True
            },
            {
                'level':'انتخاب مسافر',
                'active': True
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
    {
        'id': uuid.uuid4().hex,
        'imagePath':'macbook.jpg',
        'Title': 'مک بوک پرو 16 اینچ رتینا',
        'Origin': 'چین',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'Accept':True,
        'username':'soheil75',
        'comments':[],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': False
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': False
            },
            {
                'level':'انتخاب مسافر',
                'active': False
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
    {
        'id': uuid.uuid4().hex,
        'imagePath':'ps4.jpg',
        'Title': 'PlayStation 4 Pro 1TB Gaming Console',
        'Origin': 'ژاپن',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'Accept':False,
        'username':'soheil75',
        'comments':[
            {
                'name':'transporter',
                'rate':4,
                'data':'1/1/2020',
                'cost':100,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
            {
                'name':'transporter88',
                'rate':1,
                'data':'1/7/2020',
                'cost':150,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
        ],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': True
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': True
            },
            {
                'level':'انتخاب مسافر',
                'active': True
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
    {
        'id': uuid.uuid4().hex,
        'imagePath':'mobile.jpg',
        'Title': 'موبایل OPPO F11',
        'Origin': 'چین',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'Accept':False,
        'username':'soheil75',
        'comments':[
            {
                'name':'transporter',
                'rate':4,
                'data':'1/1/2020',
                'cost':100,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
            {
                'name':'transporter88',
                'rate':1,
                'data':'1/7/2020',
                'cost':150,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
        ],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': True
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': True
            },
            {
                'level':'انتخاب مسافر',
                'active': True
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
    {
        'id': uuid.uuid4().hex,
        'imagePath':'adidas.jpg',
        'Title': 'adidas UltraBoost road running shoe',
        'Origin': 'آلمان',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'username':'soheil75',
        'Accept':False,
        'comments':[
            {
                'name':'transporter',
                'rate':4,
                'data':'1/1/2020',
                'cost':100,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
            {
                'name':'transporter88',
                'rate':1,
                'data':'1/7/2020',
                'cost':150,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
        ],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': True
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': True
            },
            {
                'level':'انتخاب مسافر',
                'active': True
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
]
MYWARES = [
    {
        'id': uuid.uuid4().hex,
        'imagePath':'141.jpg',
        'Title': 'توپ بسکتبال مولتن مدل GL7X',
        'Origin': 'آلمان',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'Accept':False,
        'username':'soheil75',
        'comments':[
            {
                'name':'transporter',
                'rate':4,
                'data':'1/1/2020',
                'cost':100,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
            {
                'name':'transporter88',
                'rate':1,
                'data':'1/7/2020',
                'cost':150,
                'text':'کالای شما رو در اسرع وقت به دستتون میرسونم'
            },
        ],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': True
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': True
            },
            {
                'level':'انتخاب مسافر',
                'active': True
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
    {
        'id': uuid.uuid4().hex,
        'imagePath':'macbook.jpg',
        'Title': 'مک بوک پرو 16 اینچ رتینا',
        'Origin': 'چین',
        'Destination': 'ایران',
        'Url':'https://www.digikala.com/product/dkp-138368/%D8%AA%D9%88%D9%BE-%D8%A8%D8%B3%DA%A9%D8%AA%D8%A8%D8%A7%D9%84-%D9%85%D8%AF%D9%84-gl7x',
        'Value': 1,
        'Description':'توپ بسکتبال مولتن NCAA توپی بادوام که مخصوص بازی در سالن است توپ ویلسون توپی حرفه ای است که بازیکنان حرفه ای می توانند با این توپ بازی خوبی داشته باشند.',
        'Date':'10 خرداد 1399',
        'Accept':False,
        'username':'soheil75',
        'comments':[],
        'stages': [
            {
                'level':'تایید و در لیست سفارشات',
                'active': False
            },
            {
                'level':'در انتظار پیشنهاد مسافران',
                'active': False
            },
            {
                'level':'انتخاب مسافر',
                'active': False
            },
            {
                'level':'دریافت توسط مسافر',
                'active': False
            },
            {
                'level':'رسیدن مسافر به مقصد',
                'active': False
            },
            {
                'level':'تحویل به دست شرکت',
                'active': False
            },
            {
                'level':'تحویل به سفارش دهنده',
                'active': False
            },
        ]
    },
]
USER = [
    {
        'id': uuid.uuid4().hex,
        'Username': 'Jack',
        'Password': 'Password1',
    },
    {
        'id': uuid.uuid4().hex,
        'Username': 'Rowling',
        'Password': 'Password2',
    },
    {
        'id': uuid.uuid4().hex,
        'Username': 'Seuss',
        'Password': 'Password3',
    }
]

if __name__ == '__main__':
    app.run()