# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse  
from models import *
import json
import time
import datetime 
import random

def index(request):
    return render_to_response('index.html')
  
"""
3. Page should allow me to search tweets by text (full text search). 
   List of tweets should be displayed on web page in tabular format sorted by tweet date. 
   Additionally there should be date range filter if we need to select tweets within date range.
"""
def tweet_by_list(request):
    if request.method == 'GET': # If the form is submitted
        query = request.GET.get('search_box', None)

    if query != None:
        print query
        tweets = Tweets.objects.filter(text__icontains = query)
    else:
        tweets = Tweets.objects.all()
    
    for t in tweets:
        if t.place != None:
            t.place = json.loads(json.dumps(t.place))['country']
        t.username = json.loads(json.dumps(t.user))['name']  
        t.profile_pic = json.loads(json.dumps(t.user))['profile_image_url']  
    return render_to_response('table.html', {'objects': tweets}) 

"""
    2. Split of tweets by location in pie chart (percentages)
"""    
def tweet_by_location(request):
    country_dict = {}
    xdata = [] 
    ydata = []
    tweets = Tweets.objects.all()  
    for tweet in tweets:
        if tweet.place != None:
            c = json.loads(json.dumps(tweet.place))['country']
            try:
                country_dict[c] += 1
            except:
                country_dict[c] = 1 
    for c in country_dict:
        xdata.append(c)
        ydata.append(country_dict[c])

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'  # container name

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('piechart.html', data)

"""
1. Daily or weekly (whatever makes sense) no of tweets in line graph.
   Infact have both weekly view and daily view. 
   You should allow toggle between both views using dropdown selector.    
"""
def tweet_by_count(request):
    date_dict = {}
    xdata = [] 
    ydata = []
    tweets = Tweets.objects.all()  
    for tweet in tweets:
        if tweet.timestamp_ms != None:
            c = datetime.datetime.fromtimestamp(float(int(tweet.timestamp_ms)/1000)).date()
            try:
                date_dict[c] += 1
            except:
                date_dict[c] = 1
    for c in date_dict:
        xdata.append(c)
        ydata.append(date_dict[c])
    
    def start_time(x): 
        return int(time.mktime(x.timetuple()) * 1000)
    xdata = map(lambda x: start_time(x), xdata)
    
    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#a4c639'
    }
    extra_serie2 = {
        "tooltip": {"y_start": "", "y_end": " cal"},
        "date_format": tooltip_date,
        'color': '#FF8aF8'
    }
    chartdata = {'x': xdata,
                 'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1}

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d %b %Y %H',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('linechart.html', data)
