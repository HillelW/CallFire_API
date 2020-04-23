from django.shortcuts import render
from .mssql import Connect


def callfire(request):
    conn = Connect()
    db_list = conn.execute_sp_without_params('p_db_listing') 
    return render(request, 'callfire.html', {'db_list': db_list})    
