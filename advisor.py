from flask import *
from database import *
import uuid

advisor=Blueprint('advisor',__name__)

@advisor.route('/advisor_home')
def advisor_home():
    return render_template("advisor_home.html")

@advisor.route('/advisor_manage_fee',methods=['POST','GET'])
def advisor_manage_fee():
    if 'submit' in request.form:
        amt=request.form['amount']
        qry="insert into fee values(null,'%s','%s')"%(session['advisor'],amt)
        insert(qry)
        return ("<script>alert('Fee added');window.location='/advisor_manage_fee'</script>")
    data={}
    qry1="select * from fee where advisor_id='%s'"%(session['advisor'])
    res=select(qry1)
    data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

        if action == 'update':
            qry1="select * from fee where fee_id='%s'"%(id)
            res1=select(qry1)
            data['up'] = res1
            if 'update' in request.form:
                amt=request.form['amount']
                qry="update fee set amount='%s' where fee_id='%s'"%(amt,id)
                update(qry)
                return ("<script>alert('Fee updated');window.location='/advisor_manage_fee'</script>")
        if action == 'delete':
            qry2="delete from fee where fee_id='%s'"%(id)
            delete(qry2)
            return ("<script>alert('Fee deleted');window.location='/advisor_manage_fee'</script>")
    return render_template("advisor_manage_fee.html",data=data)

@advisor.route('/advisor_send_notification',methods=['POST','GET'])
def advisor_send_notification():
    if 'submit' in request.form:
        noti=request.form['noti']
        qry="insert into notification values(null,'%s','%s',curdate())"%(session['log'],noti)
        insert(qry)
        return ("<script>alert('Notification Send');window.location='/advisor_send_notification'</script>")
    return render_template("advisor_send_notification.html")

@advisor.route('/advisor_view_feedback')
def advisor_view_feedback():
    data={}
    qry1="SELECT * FROM feedback INNER JOIN USER ON feedback.sender_id = user.login_id"
    res=select(qry1)
    data['view']=res

    return render_template("advisor_view_feedback.html",data=data)

@advisor.route('/advisor_send_rating_and_review',methods=['POST','GET'])
def advisor_send_rating_and_review():
    if 'submit' in request.form:
        rating=request.form['rating']
        review=request.form['review']
        qry="insert into rating values(null,'%s','%s','%s',curdate())"%(session['log'],rating,review)
        insert(qry)
        return ("<script>alert('Review Send');window.location='/advisor_send_rating_and_review'</script>")
    return render_template("advisor_send_rating_and_review.html")
@advisor.route('/advisor_send_rating_and_review',methods=['POST','GET'])
def advisor_send_rating_and_review():
    if 'submit' in request.form:
        rating=request.form['rating']
        review=request.form['review']
        qry="insert into rating values(null,'%s','%s','%s',curdate())"%(session['log'],rating,review)
        insert(qry)
        return ("<script>alert('Review Send');window.location='/advisor_send_rating_and_review'</script>")
    return render_template("advisor_send_rating_and_review.html")

@advisor.route('/advisor_send_complaint',methods=['POST','GET'])
def advisor_send_complaint():
    if 'submit' in request.form:
        title=request.form['title']
        description=request.form['description']
        qry="insert into complaint values(null,'%s','%s','%s','pending',curdate())"%(session['log'],title,description)
        insert(qry)
        return ("<script>alert('Complaint Send');window.location='/advisor_send_complaint'</script>")
    data={}
    qry1="select * from complaint where sender_id='%s'"%(session['log'])
    res=select(qry1)
    data['view']=res
    return render_template("advisor_send_complaint.html",data=data)

@advisor.route('/advisor_offer_inv_reccomendation',methods=['POST','GET'])
def advisor_offer_inv_reccomendation():
    if 'submit' in request.form:
        video=request.files['video']
        title=request.form['title']
        description=request.form['description']

        path='static/'+str(uuid.uuid4())+video.filename
        video.save(path)

        qry="insert into inv_recomendations values(null,'%s','%s','%s','%s',curdate())"%(session['advisor'],path,title,description)
        insert(qry)
        return ("<script>alert('Invest Recommendation Added');window.location='/advisor_offer_inv_reccomendation'</script>")
    return render_template("advisor_offer_inv_reccomendation.html")

@advisor.route('/advisor_view_paid_users')
def advisor_view_paid_users():
    data={}
    qry1="select * from payment inner join user using(user_id) where status='paid' and advisor_id='%s'"%(session['advisor'])
    res=select(qry1)
    data['view']=res

    return render_template("advisor_view_paid_users.html",data=data)

@advisor.route('/advisor_view_message',methods=['POST','GET'])
def advisor_view_message():
    data={}
    qry="select * from advisor inner join chat on advisor.advisor_id = chat.receiver_id where advisor_id='%s'"%(session['advisor'])
    res=select(qry)
    
    if res:
        userid=res[0]['sender_id']
        qry2="select * from chat where (sender_type='user' and receiver_id='%s' and receiver_type='advisor') or (sender_type='advisor' and sender_id='%s' and receiver_type='user')"%(session['advisor'],session['advisor'])
        res2=select(qry2)
        if res2:
            data['view']=res2
    else:
        return '''<script>alert("no messages found");window.location="/advisor_home"</script>'''
    if 'submit' in request.form:
        message=request.form['message']
        qry1="insert into chat values(null,'%s','%s','advisor','user','%s',curdate(),curtime()) "%(session['advisor'],userid,message)
        insert(qry1)
        return redirect(url_for('advisor.advisor_view_message'))
    return render_template("advisor_chat_user.html",data=data)


@advisor.route('/advisor_view_requested_users',methods=['POST','GET'])
def advisor_view_requested_users():
    data={}
    qry1="select * from request inner join user using(user_id) where status='pending' and advisor_id='%s'"%(session['advisor'])
    res=select(qry1)
    data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

        if action == 'accept':
            qyy="select * from request where request_id='%s'"%(id)
            ress=select(qyy)
            data['up']=ress
            if 'add' in request.form:
                amt=request.form['amt']
                qry="update request set status='request accepted',amount='%s' where request_id='%s'"%(amt,id)
                update(qry)
                return ("<script>alert('Request accepted');window.location='/advisor_view_requested_users'</script>")
        if action == 'reject':
            qry2="update request set status='request rejected' where request_id='%s'"%(id)
            delete(qry2)
            return ("<script>alert('Request rejected');window.location='/advisor_view_requested_users'</script>")

    return render_template("advisor_view_requested_users.html",data=data)



#import cryptocompare
#import pandas as pd
#import numpy as np
#from datetime import datetime
#from sklearn.preprocessing import MinMaxScaler
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import LSTM, Dense, Dropout
#from flask import Flask, request, render_template


