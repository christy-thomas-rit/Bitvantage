from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template("admin_home.html")

@admin.route('/admin_verify_advisor')
def admin_verify_advisor():
    data={}
    qry="select * from advisor inner join login using(login_id)"
    res=select(qry)
    data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

        if action == 'verify':
            qry1="update login set usertype='advisor' where login_id='%s'"%(id)    
            update(qry1)
            return ("<script>alert('Advisor verified');window.location='/admin_verify_advisor'</script>")
        if action == 'reject':
            qry1="update login set usertype='rejected' where login_id='%s'"%(id)
            update(qry1)
            return ("<script>alert('Advisor Rejected');window.location='/admin_verify_advisor'</script>")
    return render_template("admin_verify_advisor.html",data=data)

@admin.route('/admin_send_notification',methods=['POST','GET'])
def admin_send_notification():
    if 'submit' in request.form:
        noti=request.form['noti']
        qry="insert into notification values(null,'%s','%s',curdate())"%(session['log'],noti)
        insert(qry)
        return ("<script>alert('Notification Send');window.location='/admin_send_notification'</script>")
    return render_template("admin_send_notification.html")

@admin.route('/admin_view_complaints', methods=['POST', 'GET'])
def admin_view_complaints():
    data = {}
    qry = "select * from complaint"
    res = select(qry)
    if res:
        complaints = []
        for complaint in res:
            sender_id = complaint['sender_id']
            sender_name = ""

            # Check sender_id in each possible sender table
            qry_sender = "select name from advisor where login_id='%s'" % sender_id
            sender_res = select(qry_sender)
            if sender_res:
                sender_name = sender_res[0]['name']
            else:
                qry_sender = "select name from user where login_id='%s'" % sender_id
                sender_res = select(qry_sender)
                if sender_res:
                    sender_name = sender_res[0]['name']

            complaint['sender_name'] = sender_name
            complaints.append(complaint)

        data['view'] = complaints

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

        if action == 'reply':
            qry1="select * from complaint where complaint_id='%s'"%(id)
            res1=select(qry1)
            data['up'] = res1
            if 'submit' in request.form:
                reply=request.form['reply']
                qry="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
                update(qry)
                return ("<script>alert('reply send successfully');window.location='/admin_view_complaints'</script>")

    return render_template("admin_view_complaints.html", data=data)

@admin.route('/admin_view_rating')
def admin_view_rating():
    data = {}
    qry = "select * from rating"
    res = select(qry)
    if res:
        ratings = []  # Renamed from 'rating' to 'ratings'
        for rating in res:
            sender_id = rating['sender_id']
            sender_name = ""

            # Check sender_id in each possible sender table
            qry_sender = "select name from advisor where login_id='%s'" % sender_id
            sender_res = select(qry_sender)
            if sender_res:
                sender_name = sender_res[0]['name']
            else:
                qry_sender = "select name from user where login_id='%s'" % sender_id
                sender_res = select(qry_sender)
                if sender_res:
                    sender_name = sender_res[0]['name']

            # Ensure 'rating' is an integer
            try:
                rating['rating'] = int(rating.get('rating', 0))
            except ValueError:
                rating['rating'] = 0

            rating['sender_name'] = sender_name
            ratings.append(rating)  # Append the dictionary to the list

        data['view'] = ratings

    return render_template("admin_view_rating.html", data=data)



