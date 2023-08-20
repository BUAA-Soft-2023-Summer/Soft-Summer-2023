import json
from datetime import datetime, date

from django.http import JsonResponse
from api.models import ItemInfo


# 新建计划
def create(request):
    # 获取传入的基本信息
    data = json.loads(request.body)
    title = data.get('title')
    content = data.get('content')
    endTime = data.get('endTime')
    try:
        if title is None or endTime is None:
            return JsonResponse({'message': 'fail', 'error': 'message missing'}, status=400)
        ItemInfo.objects.create(title=title,
                                content=content,
                                status=False,
                                createTime=datetime.now(),      # 获取当前时间
                                endTime=endTime)
        return JsonResponse({'message': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'message': 'fail', 'error': str(e)}, status=400)


# 删除计划
def delete(request):
    # 获取基础信息
    data = json.loads(request.body)
    ID = data.get('ID')
    try:
        # 检查是否有该条计划
        cnt = ItemInfo.objects.filter(ID=ID).count()
        if cnt == 0:
            return JsonResponse({'message': 'fail', 'error': 'ID is not exist'}, status=422)
        ItemInfo.objects.get(ID=ID).delete()
        return JsonResponse({'message': 'success'}, status=200)
    except Exception as e:
        return JsonResponse({'message': 'fail', 'error': str(e)}, status=400)


# 修改计划
def update(request):
    data = json.loads(request.body)
    ID = data.get('ID')
    title = data.get('title')
    content = data.get('content')
    status = data.get('status')
    endTime = data.get('endTime')

    obj = ItemInfo.objects.get(ID=ID)
    if obj is None:
        return JsonResponse({'message': 'fail', 'error': 'title is not exist'}, status=422)
    if title is not None:
        obj.title = title
    if content is not None:
        obj.content = content
    if endTime is not None:
        obj.endTime = endTime
    if status is not None:
        obj.status = status
    obj.save()
    return JsonResponse({'message': 'success'}, status=200)

def searchByID(request):
    data = json.loads(request.body)
    ID = data.get('ID')
    obj = ItemInfo.objects.get(ID=ID)
    if obj is None:
        return JsonResponse({'message': 'fail', 'error': 'ID is not exist'}, status=422)
    return JsonResponse({
        'ID': obj.ID,
        'title': obj.title,
        'content': obj.content,
        'status': obj.status,
        'createTime': obj.createTime.strftime("%Y-%m-%d %H:%M:%S"),     # 人为设定返回的日期格式
        'endTime': obj.endTime
    }, status=200)

def getJson(answer):
    result = []
    for item in answer:
        # answer 是一个 QuerySet 对象，需要遍历把每一项取出来，然后再得到有用信息
        title = item.title
        endTime = item.endTime
        status = item.status    # new
        ID = item.ID
        # 每一条信息形成字典后加入到 result 中
        info = {
            'ID': ID,
            'title': title,
            'status': status,   # new ,返回值是一个 boolean
            'endTime': endTime
        }
        result.append(info)
    return JsonResponse({'message': 'success', 'result': result}, status=200)


# 根据日期查找
def searchByDate(request, year, month, day):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'invalid request'}, status=400)

    time = date(year, month, day)
    # 将内容首先按照 endTime 升序排列以后筛选 endTime <= time 的内容
    answer = ItemInfo.objects.order_by('endTime').filter(endTime__lte=time)
    return getJson(answer)


def getAll(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'invalid request'}, status=400)

    answer = ItemInfo.objects.order_by('endTime')
    return getJson(answer)
