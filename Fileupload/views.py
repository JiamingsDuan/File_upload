from django.shortcuts import render
# from django.shortcuts import HttpResponse
from django.shortcuts import redirect


def index(request):

    if request.method == "GET":
        return render(request, 'index.html')

    else:

        # 包含用户提交的所有信息
        # 获取用户提交方法
        # print(request.method)
        error_msg = ""
        if request.method == "POST":
            # 获取用户通过POST提交过来的数据
            username = request.POST.get('login[username]', None)
            password = request.POST.get('login[password]', None)
            print('用户名:', username, '密码:', password)
            if username == 'root@root.com' and password == "123456":
                # 去跳转到
                return redirect('/app01/upload')
            else:
                # 用户密码不配
                error_msg = "用户名或密码错误"
        return render(request, 'index.html', {'error_msg': error_msg})


def register(request):

    return render(request, 'register.html')
