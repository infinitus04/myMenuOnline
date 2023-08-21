import functools
from client.models import *
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect, HttpResponse
import uuid
from utilityCodes import qrCodeGenrator

def menu_creation(view_func, verification_url="/client/getstarted/"):

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if Menu.objects.filter(user=request.user).exists():
            return view_func(request, *args, **kwargs)
        messages.info(request, "create menu first")
        print("create menu first")
        return redirect(verification_url)
    return wrapper


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
                data = {
                    'invalid_credentials':True
                }
                return render(request, 'client/login.html', data)
        return render(request, 'client/login.html')
    return redirect('/client/psudoPanel')



def clientLogout(request):
    logout(request)
    return redirect('/client/login')



@login_required
@menu_creation
def psudoPanel(request):
    
    # print(request.user)
    menu = Menu.objects.get(user = request.user)
    dailyVisitors = DailyVisitors.objects.get(menu = menu) 

    data = {
        'menu' : menu,
        'dailyVisitors': dailyVisitors
    }
    
    return render(request, 'client/psudoPanel.html', data)

@login_required
@menu_creation
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
            
            messages.success(request, 'Category created sucessfully!')
            return redirect('/client/category/')
        else:
            print('empty hai not allowed')
    return render(request, 'client/categoryAdd.html')

@login_required
@menu_creation
def categoryList(request):
    menu = Menu.objects.get(user= request.user)
    # print(menu)
    headers = Header.objects.filter(menu = menu)
    return render(request, 'client/categoryList.html', {'headers': headers})


@login_required
@menu_creation
def categoryEdit(request, id):
    header = Header.objects.get(id = id)
    if request.method =="POST":
        
        if 'saveSubmit' in request.POST:
        # If submit buttton is clicked
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
            messages.success(request, 'Item edited sucessfully!')
            return redirect('/client/category/')
        
        elif 'deleteSubmit' in request.POST:
            messages.error(request, 'Item deleted sucessfully!')
            header.delete()
            return redirect('/client/category/')

    if header.menu.user==request.user:
        return render(request, 'client/categoryEdit.html', {'header': header})
    else:
        return HttpResponse('you are forbidden to visit this page :(')

# Item view functions

@login_required
@menu_creation
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
@menu_creation
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
            vegnonveg = request.POST.get('vegnonveg')
            tags = request.POST.get('tags')

            Item.objects.create(
                item_name=itemName,
                price = price,
                vegnonveg = vegnonveg,
                tags = tags,
                header = header
            )
            messages.success(request, 'Item added sucessfully')
            
            if 'save' in request.POST:
                return redirect(f'/client/items/category={header.id}/')
            elif 'saveandnew' in request.POST:
                return redirect(f'/client/items/category={header.id}/add/')


        return render(request, 'client/itemAdd.html', {'header': header })

@login_required
@menu_creation
def itemEdit(request, id, itemId):
    
    try:
        header = Header.objects.get(id = id)
        item = Item.objects.get(id = itemId)
    except:
        return HttpResponse('404 page not found')
    if header.menu.user != request.user or item.header != header:
        return HttpResponse('You are not authorized to view this page')

    if request.method == 'POST':
        
        if 'saveSubmit' in request.POST:
            itemName = request.POST.get('itemName')
            price = request.POST.get('price')
            tags = request.POST.get('tags')
            vegnonveg = request.POST.get('vegnonveg')

            if item.item_name != itemName:
                item.item_name = itemName
            if item.price != price:
                item.price = price
            if item.tags != tags:
                item.tags = tags
            if item.vegnonveg != vegnonveg:
                item.vegnonveg = vegnonveg
            item.save()
            messages.success(request, 'Item edited sucessfully!')
            
        elif 'deleteSubmit' in request.POST:
            item.delete()
            messages.error(request, 'Item deleted sucessfully!')
        
        return redirect(f'/client/items/category={header.id}/')
        # print(f'itemname: {itemName} | price: {price} | tags: {tags} | vegnonveg: {vegnonveg}')

    return render(request, 'client/itemEdit.html',{'header': header, 'item': item })

@login_required 
def menuCreation(request):
    if 'changePassword' in request.POST:
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        saveuser = CustomUser.objects.get(id = request.user.id)
        if (old_password and new_password) and (new_password==confirm_password):
            if request.user.check_password(old_password):
                saveuser.set_password(new_password)
                update_session_auth_hash(request, saveuser)
                saveuser.save()
                print('Password changed sucessfully')
                messages.success(request, 'Password changed sucessfully')
                return redirect('/client/getstarted/details/')
            else:
                messages.error(request, 'Old password is incorrect')
                return redirect('/client/getstarted/')
        
        print(f'{old_password} | {new_password} | {confirm_password}')
        return redirect('/client/getstarted/')
    return render(request, 'client/menuCreation.html')

@login_required 
def regMenuDetail(request):
    if request.method == "POST":
        instance = Menu()
        instance.user = request.user
        Template.objects.all()
        instance.template = Template.objects.all()[:1].get()
        menu_link = uuid.uuid4().hex
        print(menu_link)
        instance.menu_link = menu_link 
        qr_link = qrCodeGenrator.qr_code_create((menu_link))
        instance.qrcode = qr_link

        instance.logo = request.FILES.get('logo')
        
        if request.POST.get('business_name'):
            instance.business_name = request.POST.get('business_name')
        else:
            messages.error('Business name cannot be empty')
            return redirect('/client/getstarted/details/')


        if request.POST.get('business_contact_number'):
            instance.business_contact_number = request.POST.get('business_contact_number')

        if request.POST.get('address'):
            instance.address = request.POST.get('address')

        if request.POST.get('instagram_link'):
            instance.instagram_link = request.POST.get('instagram_link')

        if request.POST.get('facebook_link'):
            instance.facebook_link = request.POST.get('facebook_link')

        if request.POST.get('google_link'):
            instance.google_link = request.POST.get('google_link')
        
        instance.save()
        DailyVisitors.objects.create(menu= instance)
        return redirect('/client/psudoPanel/')

    return render(request, 'client/regMenuDetails.html')


