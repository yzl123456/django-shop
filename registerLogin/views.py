# coding=utf-8
from django.shortcuts import render
from django.http import *
from cart.models import *
from detail.models import *
from goodslist.models import *
from index.models import *
from registerLogin.models import *
from usercenter.models import *
from datetime import datetime
from usercenter import der
import hashlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter






# 验证码测试页
def verify(request):
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def verify_check2(request):
    """验证码的验证"""
    # 1.获取post请求当中的输入验证码的内容
    verify = request.POST.get('verify')
    # 2.获取浏览器请求当中的session中的值
    verifycode = request.session.get('verifycode')
    # 3.判断两个验证码是否相同
    if verify == verifycode:
        return HttpResponse('ok')
    else:
        return HttpResponse('err')


def show_verify2(request):
    """显示验证码界面"""
    return render(request, 'freshFruit/verify.html')

def index(request):
    print("index---------")
    return render(request, 'freshFruit/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'freshFruit/register.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        password = request.POST.get('pwd', None)
        email = request.POST.get('email', None)
        if user_name and len(password) >= 8 and email:
            try:
                if UserInfo.objects.get(uName=user_name):
                    pass
            except Exception as e:
                user = UserInfo()
                user.uName = user_name
                n = hashlib.md5()
                n.update(password.encode("utf8"))

                user.uPassword = n.hexdigest()

                user.uEmail = email
                user.uRegDate = datetime.now()
                user.save()

                print('写入完成')
                return HttpResponseRedirect('/login/')
            else:
                print('user has exis:不允许注册')
                return render(request, 'freshFruit/register.html')
            finally:
                pass


def regcheck(request):
    name = request.GET.get('name', None)
    if name:
        try:
            if UserInfo.objects.get(uName=name):
                pass
        except Exception as e:
            print('exception:注册用户不存在可以注册')
            return JsonResponse({'find': 'False'})
        else:
            print('user has exis:不允许注册')
            return JsonResponse({'find': 'True'})
        finally:
            pass
    else:
        return HttpResponse('未接受到数据')


@der.login_name
def login(request, dic):
    if request.method == 'GET':
        return render(request, 'freshFruit/login.html', dic)
    elif request.method == 'POST':
        name = request.POST.get('username', None)
        password = request.POST.get('pwd', None)
        vecode = request.POST.get('ucode')
        # 先验证验证码防止暴力破解
        if vecode.upper() != request.session['verifycode']:
            return render(request, 'freshFruit/login.html', {'error': {'password': '验证码错误'}})
        if name and password:

            user = UserInfo.objects.get(uName=name)
            # 如果用户密码和验证都正确，登陆成功
            n = hashlib.md5()
            n.update(password.encode("utf8"))
            if user.uPassword == n.hexdigest():
                if request.POST.get('check', None) == 'on':
                    request.session['name'] = name
                # request.session['password'] = password    #状态保持
                else:
                    request.session['name'] = name
                    request.session.set_expiry(0)  # 超时测试
                return HttpResponseRedirect('/index/')
            else:
                return render(request, 'freshFruit/login.html', {'error': {'password': '密码输入有误，请重新输入'}})

        else:
            return render(request, 'freshFruit/login.html', {'error': {'name': '请输入用户名', 'password': '请输入密码'}})


# 密码修改
def changekw(request):
    if request.method == 'GET':
        return render(request, 'freshFruit/changekw.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        password = request.POST.get('pwd', None)
        email = request.POST.get('email', None)
        if user_name and len(password) >= 8 and email:
            auser = UserInfo.objects.get(uName=user_name)
            if auser.uEmail == email:
                n = hashlib.md5()
                n.update(password)
                auser.uPassword = n.hexdigest()
                auser.save()
                return HttpResponseRedirect('/login/')
            else:
                return render(request, 'freshFruit/changekw.html', {'error': {'email': '邮箱错误，请重新输入'}})

    return render(request, 'freshFruit/changekw.html')
