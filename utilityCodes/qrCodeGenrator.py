import qrcode,os

def qr_code_create(image):
    link = 'http://127.0.0.1:8000/' + str(image)
    qr = qrcode.make(link)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # qr.add_data('Scan for menu')
    path = BASE_DIR + f'/media/qrcodes/{image}.png'
    qr.save(path)
    return(f'/qrcodes/{image}.png')

# print(Site.objects.get_current().domain)
# qr_code_create(image='lelelavde')