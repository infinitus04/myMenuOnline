from django.shortcuts import render, HttpResponse
from client.models import Menu, Header, Item, DailyVisitors
from django.db.models import F

# Create your views here.
def serve(request, linkId):
    # menu  = ''
    try:
        menu = Menu.objects.get(menu_link = linkId)
    except:
        return HttpResponse('404 page not found', status= 404)
    if menu.is_subscribed:

        data = {}
        data['menu'] = menu
        # print(f'link is {menu_obj.menu_link}')
        headers = Header.objects.filter(menu = menu)
        # print(menu_obj)
        h = []
        for head in headers:
            headers = {}
            headers['header'] = head
            items = Item.objects.filter(header = head).order_by('price')
            allitem = []
            for item in items:
                allitem.append(item)
            headers['item']=allitem
            h.append(headers)
        data['headers'] = h

        template_name = menu.template.template_file_name

        dailyVisitors = DailyVisitors.objects.get(menu=menu)
        # print(dailyVisitors)
        if DailyVisitors:
            dailyVisitors.Daily_visitors= dailyVisitors.Daily_visitors +1
            dailyVisitors.save()

        return render(request, template_name, data)
        
    else:
        return render(request, 'user/notsub.html')