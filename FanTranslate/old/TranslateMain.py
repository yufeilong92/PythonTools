import requests
from urllib.parse import urlencode
import execjs
import time
import json


class TranslateMain:
    # 处理请求头
    def getHeaders(slef,cookies):
        headers = {
            'Host': 'fanyi.baidu.com',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Cookie': cookies
        }
        return headers


    # 处理cookies
    def getCookies(slef,t):
        # cookies = 'BAIDUID=2798F941BEE3BAD44CC9E6225279FF4A:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=' + t + '; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=' + t + ';'
        cookies = 'BAIDUID=09244CE8ADD5137FB97F52AD6A82BF81:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=' + t + '; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=' + t + ';'
        return cookies


    # 取sign，用到了execjs模块
    def getSign(slef,wd):

        # return r
        ctx = execjs.compile("""
        window = {};
        var i = null;
        function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var a = o.charAt(t + 2);
                a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
            }
        }
        function e(r) {
            var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
            if (null === o) {
                var t = r.length;
                t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
            } else {
                for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++) "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
                var g = f.length;
                g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
            }
            var u = void 0,
                l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
            u = null !== i ? i : (i = window[l] || "") || "";
            u = '320305.131321201';
            for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                var A = r.charCodeAt(v);
                128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                S[c++] = A >> 18 | 240,
                S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                S[c++] = A >> 6 & 63 | 128),
                S[c++] = 63 & A | 128)
            }
            for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
            p = n(p, F);
            return p = n(p, D),
            p ^= s,
            0 > p && (p = (2147483647 & p) + 2147483648),
            p %= 1e6,
            p.toString() + "." + (p ^ m)
        }
        """)
        return ctx.call("e", wd)


    # 取输入的语言
    def getLan(slef,wd, headers):
        url = "https://fanyi.baidu.com/langdetect"
        data = {'query': wd}
        # 对post提交的表单进行url编码
        resp = requests.post(url, data=urlencode(data).encode("utf-8"), headers=headers)
        lan = ''
        # 如果状态码 == 200 就说明正常请求正常
        if resp.status_code == 200:
            # json解析
            data_json = json.loads(resp.text)
            msg = data_json['msg']
            if msg == "success":
                lan = data_json['lan']
        else:
            print(resp.text)

        return lan


    def fanyi(slef,wd, lan, sign, token, headers):
        language = ""
        # if lan == 'zh':
        #     language = "zh"
        # elif lan == 'en':
        #     language = "zh"
        # elif lan =='jp':
        #     language='zh'
        # else:
        #     language = "zh"
        lan = 'jp'
        language = 'zh'
        url = "https://fanyi.baidu.com/v2transapi?from=" + lan + "&to=" + language
        # print(url)
        data = {
            'from': lan,
            'to': language,
            'query': wd,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': token,
            'domain': 'common'
        }
        resp = requests.post(url=url, data=urlencode(data).encode("utf-8"), headers=headers)
        retdata = ""
        if resp.status_code == 200:
            print("请求成功")
            retdata = (resp.text.encode("utf-8"))
        return retdata


    def getToken(slef,headers):
        url = "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh"
        resp = requests.get(url, headers=headers)
        print(resp.text)
        # 这里我偷懒了自己取一下返回的token吧

    def getTranslate(self,data):
        t = round(time.time())
        
        cookies = self.getCookies(str(t))
        headers = self.getHeaders(cookies)
        # getToken(headers)
        wd=data
        lan = self.getLan(wd, headers)
        sign = self.getSign(wd)
        # json_data =self. fanyi(wd, lan, sign, '97f41ef953422689ecd99065d10c7775', headers)
        json_data =self. fanyi(wd, lan, sign, '97cb2a7ff99e90e49c0877700d548c5e', headers)

        try:
            json_data = json.loads(bytes(json_data).decode("utf-8"))
            print(json_data)
            return  json_data['trans_result']['data'][0]['dst']
        except Exception as e:
            print(e)
            return  None
        pass
    # if __name__ == "__main__":
    #     # 取10位时间戳
    #     t = round(time.time())
    #     cookies = getCookies(str(t))
    #     headers = getHeaders(cookies)
    #     # getToken(headers)
    #     wd = input("请输入要翻译的内容:")
    #     lan = getLan(wd, headers)
    #     sign = getSign(wd)
    #     json_data = fanyi(wd, lan, sign, '97f41ef953422689ecd99065d10c7775', headers)
    #
    #     json_data = json.loads(bytes(json_data).decode("utf-8"))
    #     print(json_data['trans_result']['data'][0]['dst'])
