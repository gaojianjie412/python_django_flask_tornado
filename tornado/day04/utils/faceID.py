
from aip import AipFace

""" 你的 APPID AK SK """
APP_ID = '15754452'
API_KEY = 'RxIgwAqrCbHDhTLGn41iobHF'
SECRET_KEY = 'MGxV54ncRmiyevlrjZiDcU1OwEeupVKT'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_register(image, userId, imageType='BASE64', groupId='user'):

    """ 调用人脸注册 """
    res = client.addUser(image, imageType, groupId, userId)
    print(res)
    if res['error_code']:
        # 注册失败
        return False
    # 注册成功
    return True


def face_login(image, imageType='BASE64', groupId='user'):
    """ 调用人脸检索接口 """
    res = client.search(image, imageType, groupId)
    print(res)
    if res['error_code']:
        return False
    return True
