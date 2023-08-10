from django.shortcuts import render, redirect, HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from client.models import *

# Create your views here.
def clientLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            # user = CustomUser.objects.get(phone= username)
            
            user = authenticate(request, phone= phone, password = password)
            if user is not None:
                login(request, user)
                return redirect('/client/psudoPanel/')
            else:
                print(f'no user found')
        return render(request, 'client/login.html')
    return redirect('/client/psudoPanel')



def clientLogout(request):
    logout(request)
    return redirect('/client/login')



@login_required
def psudoPanel(request):
    
    # print(request.user)
    menu_link = Menu.objects.get(user = request.user).menu_link
    templates = Template.objects.all()

    data = {
        'menu_link' : menu_link,
        'templates': templates
    }
    
    return render(request, 'client/psudoPanel.html', data)

@login_required
def categoryAdd(request):
    if request.method == 'POST':
        category_name = request.POST.get('categoryName')
        imagee = request.FILES.get('image')
        description = request.POST.get('description')
        # print(f'name:{category_name} | image:{imagee} | desc:{description}')

        menu = Menu.objects.get(user = request.user)
        if (category_name != None) and (category_name != "") and (menu is not None):
            header = Header()
            header.header_text = category_name
            header.description = description
            header.menu = menu
            header.image = imagee
            header.save()
            return redirect('/client/category/')
        else:
            print('empty hai not allowed')
    return render(request, 'client/categoryAdd.html')

@login_required
def categoryList(request):
    menu = Menu.objects.get(user= request.user)
    # print(menu)
    headers = Header.objects.filter(menu = menu)
    return render(request, 'client/categoryList.html', {'headers': headers})


@login_required
def categoryEdit(request, id):
    header = Header.objects.get(id = id)
    if request.method =="POST":
        categoryName = request.POST.get('categoryName')
        description =  request.POST.get('description')
        imagee = request.FILES.get('image')
        print(f'Name: {categoryName} | dis: {description} | image: {imagee}')
        if imagee:
            header.image = imagee

        if header.header_text != categoryName:
            header.header_text = categoryName
        
        if header.description != description:
            header.description = description

        header.save()
        return redirect('/client/category/')
    
    if header.menu.user==request.user:
        return render(request, 'client/categoryEdit.html', {'header': header})
    else:
        return HttpResponse('you are forbidden to visit this page :(')

# Item view functions

@login_required
def itemList(request, id):
    try:
        header = Header.objects.get(id = id)
    except:
        return HttpResponse('404 page not found')
    if header.menu.user == request.user:
        items = Item.objects.filter(header= header).order_by('price')
        print(items)

        data = {
            'header' : header,
            'items': items,
        }
        return render(request, 'client/itemList.html',data )

    else:
        return HttpResponse('You are not authorized to view this page')
        
@login_required    
def itemAdd(request, id):
    try:
        header = Header.objects.get(id = id)
    except:
        return HttpResponse('404 page not found')
    if header.menu.user != request.user:
        return HttpResponse('You are not authorized to view this page')
    else:
        if request.method == "POST":
            itemName = request.POST.get('itemName')
            price = request.POST.get('price')
            vegnonveg = 'veg'
            tags = request.POST.get('tags')

            # print(f'name: {itemName} | price: {price} | desc:{vegnonveg} | tags: {tags}')
            Item.objects.create(
                item_name=itemName,
                price = price,
                vegnonveg = vegnonveg,
                tags = tags,
                header = header
            )
            return redirect(f'/client/items/{header.id}/')


        return render(request, 'client/itemAdd.html', {'header': header })