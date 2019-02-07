# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from restaurant.models import Table, Booking
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


#################################
## Show Booked table lists
#################################
class BookListView(ListView):
    model = Booking
    template_name = 'books/booking_list.html'
    context_object_name = 'books'  # Default: object_list
    paginate_by = 10
    queryset = Booking.objects.all()

###########################################
## Create table
###########################################
def create_tables(request):
    table_data = Table.objects.all()
    if request.method == 'POST':
    	status_data = {}
        data_list = request.POST.getlist('form_data[]')
        data_id_list = request.POST.getlist('form_data_id[]')
        for (key, data) in enumerate(data_list):
            try:
                if data_id_list[key] == '0' and data != '':
                    c = Table(name=data)
                    c.save()
                    status_data['status'] = True  # success
                if data_id_list[key] != '0':
                    c = Table.objects.get(id=data_id_list[key])
                    c.name = data
                    c.save()
                    status_data['status'] = True
            except:
                status_data['status'] = False  # failed
        return JsonResponse(status_data)
    data={
        'table_data': table_data
    }
    return render(request, 'books/create_table.html', {'data': data})

########################################
## Create booking table and store it
########################################
def book_table(request):
    table_data = Table.objects.all()
    booking_data={}
    if request.method == 'POST':
            name = request.POST.get('table_name', None)
            start_time = request.POST.get('start_time', None)
            end_time = request.POST.get('end_time', None)
            try:
	            BookingSave = Booking(table_id=name, booking_time_start=start_time, booking_time_end=end_time)
	            BookingSave.save()
	            booking_data['status'] = True
            except:
            	booking_data['status'] = False
            return JsonResponse(booking_data)
    data={
        'table_data': table_data
    }
    return render(request, 'books/create_booking.html', {'data': data})

#########################################
## Check the given time exist or not 
##########################################
@csrf_exempt
def existing_time_check(request):
	data={}
	given_time = request.POST.get('start_time', None)
	exist_count = Booking.objects.filter(booking_time_start__lte=given_time, booking_time_end__gte=given_time).count()
	data['count'] = exist_count
	return JsonResponse(data)
    

