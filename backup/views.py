__author__ = 'sype'



from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.forms.widgets import RadioSelect
from django.forms.fields import ChoiceField
from clusterlib.dump_mysql import *
import os
from django import forms
import MySQLdb


db = MySQLdb.connect(host="10.7.20.3", # your host, usually localhost
    user="spincemail", # your username
    passwd="Seb4sB9oXx", # your password
    db="information_schema") # name of the data base

NODE_CHOICE = (
    ('1', 'node01'),
    ('2', 'node02'),
)



class BackupForm(forms.Form):
    hostname = forms.ChoiceField(widget=RadioSelect, choices= NODE_CHOICE)
    emplacement = forms.CharField()
    schema = forms.CharField()



def backup(request):
    if request.method == 'POST':
        form = BackupForm(request.POST)
        if form.is_valid():
            hostname = form.cleaned_data['hostname']
            emplacement = form.cleaned_data['emplacement']
            schema = form.cleaned_data['schema']



        return  redirect('success/')


    else:
        form = BackupForm()

    return  render_to_response('backup.html', {'form': form}, context_instance=RequestContext(request))



















def success(request):

    message = 'success'

    #return HttpResponse('success')
    return render_to_response('backup.html', {'message': message}, context_instance=RequestContext(request))










def check_stats(request):
    """


    """
    dict={}
    cur = db.cursor()
    message = "NODE01"


 # Use all the SQL you like
    cur.execute("SHOW status;")


    for row in cur.fetchall():
        #dict.setdefault(row[0],[]).append(row[1])
        #if dict["wsrep_local_state_comment"] == ['Synced']:
            sync_state =  "cluster synchronised"
            #if dict['wsrep_cluster_size'] == ['2']:
             #   size_cluster =  " All node are up"

            #if dict['wsrep_ready'] == ['ON']:
             #    connection_state = "Node ready for connection"

    #return render_to_response('backup.html', {'dict': dict,'cluster_name':message}, context_instance=RequestContext(request))
