from django.shortcuts import render, HttpResponse
from client.models import Menu, Header, Item

# Create your views here.
def serve(request, linkId):
    menu = Menu.objects.get(menu_link = linkId)
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
            items = Item.objects.filter(header = head)
            allitem = []
            for item in items:
                allitem.append(item)
            headers['item']=allitem
            h.append(headers)
        data['headers'] = h
        # print(data)
        template_name = menu.template.template_file_name
        return render(request, template_name, data)
        
    else:
        return render(request, 'user/notsub.html')