
import  re
import  execjs
import requests

session=requests.session()
index_url='https://fanyi.baidu.com'
lang_url='https://fanyi.baidu.com/langdetect'
transalte_api='https://fanyi.baidu.com/v2transapi?'
headers={
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}



def get_params(query):

    session.get(url=index_url,headers=headers)
    response_index = session.get(url=index_url, headers=headers)
    token=re.findall(r"token: '([0-9a-z]+)'",response_index.text)[0]
    print(f"token==={token}")
    gtk = re.findall(r'gtk = "(.*?)"', response_index.text)[0]
    print(f"window.gtk={gtk},window.token={token}")
    #自动检测语音
    response_lang=session.post(url=lang_url,headers=headers,data={'query':query})
    lang=response_lang.json()['lan']
    return token,gtk,lang
def get_sign(query,gtk):
    with open("baiduSign.js",'r',encoding='utf-8')as f:
        baidu_js=f.read()
    sign=execjs.compile(baidu_js).call('b',query,gtk)
    return sign

def get_result(query ,lang,sign,token):
    data={
        'from': 'jp',
        # 'from': lang,
        'to': 'zh',
        'query': query,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': sign,
        'token': token,
        'domain': 'common'
    }
    response = session.post(url=transalte_api, headers=headers, data=data)
    print(response.json())
    result = response.json()['trans_result']['data'][0]['dst']
    return result

if __name__ == '__main__':
    query=input("请输入")
    token,gtk,lang = get_params(query)
    print(f"==token=={token}={gtk}=={lang}")
    sign = get_sign(query, gtk)
    print(f"=sign==={sign}")
    result = get_result(query, lang, sign, token)
    print(result)
    pass