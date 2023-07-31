from django.http import HttpResponse, JsonResponse


# Create your views here.


def hello_world(request):
    return HttpResponse('hello world')


def hello_china(request):
    return HttpResponse('hello china')


def article_list(request, month):
    """
    :param month: 今年某一个月的文章列表
    """
    return HttpResponse('article {}'.format(month))


def search(request):
    """GET参数的获取"""
    name = request.GET.get('name', '')
    print('name --------->>>>>>>>>>>>>', name)
    return HttpResponse('查询成功！')


def http_request(request):
    """请求练习"""
    # 1、请求方式
    print('请求方式 ----------->>>>>>>>>', request.method)
    # 2、请求头信息
    headers = request.META
    print('请求头信息 ----------->>>>>>>>>', headers)
    # 获取 user-agent
    ua = request.META.get('HTTP_USER_AGENT', None)
    print('user-agent -------->>>>>>>>>', ua)
    print('user-agent -------->>>>>>>>>', request.headers['User-Agent'])
    print('user-agent -------->>>>>>>>>', request.headers['user-agent'])
    # 3、获取请求参数
    name = request.GET.get('name', '没有传递参数的默认值')
    print('获取请求参数 ----------->>>>>>>>>', name)
    return HttpResponse('响应！')


def http_response(request):
    """响应练习"""
    # resp = HttpResponse('响应内容', status=201)
    # resp.status_code = 200
    # print('resp.status_code ----->>>>>', resp.status_code)
    # return resp

    user_info = {
        'name': '张三',
        'age': 34
    }
    return JsonResponse(user_info)



