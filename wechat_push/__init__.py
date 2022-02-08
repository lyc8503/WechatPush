import requests
import time


class WechatPush:
    def __init__(self, corp_id, secret, agent_id):
        self.corp_id = corp_id
        self.agent_id = agent_id
        self.secret = secret
        self.token = ''
        self.expire = 0

    def refresh_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params={
            "corpid": self.corp_id,
            "corpsecret": self.secret
        }).json()
        access_token = r['access_token']
        if access_token and len(access_token) > 0:
            self.token = access_token
            self.expire = r['expires_in'] + time.time() - 10

    def refresh_token_if_expire(self):
        if time.time() > self.expire:
            self.refresh_token()

    def send_text(self, text, to_uid='@all'):
        self.refresh_token_if_expire()
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send', params={
            'access_token': self.token
        }, json={
            "touser": to_uid,
            "agentid": self.agent_id,
            "msgtype": "text",
            "text": {
                "content": text
            },
            "duplicate_check_interval": 600
        }).json()
        return r

    def send_image(self, image_file, to_uid='@all'):
        self.refresh_token_if_expire()
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload", params={
            "access_token": self.token,
            "type": "image"
        }, files={
            "picture": image_file
        }).json()
        if "media_id" in r:
            media_id = r['media_id']
        else:
            raise Exception("failed to upload: " + str(r))

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send", params={
            "access_token": self.token
        }, json={
            "touser": to_uid,
            "agentid": self.agent_id,
            "msgtype": "image",
            "image": {
                "media_id": media_id
            },
            "duplicate_check_interval": 600
        }).json()
        return r

    def send_markdown(self, markdown, to_uid='@all'):
        self.refresh_token_if_expire()
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send", params={
            "access_token": self.token
        }, json={
            "touser": to_uid,
            "agentid": self.agent_id,
            "msgtype": "markdown",
            "markdown": {
                "content": markdown
            },
            "duplicate_check_interval": 600
        }).json()
        return r

    def send_file(self, file, filename="文件", to_uid='@all'):
        self.refresh_token_if_expire()
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/media/upload", params={
            "access_token": self.token,
            "type": "file"
        }, files={
            "media": (filename, file)
        }).json()

        if "media_id" in r:
            media_id = r['media_id']
        else:
            raise Exception("failed to upload: " + str(r))

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send", params={
            "access_token": self.token
        }, json={
            "touser": to_uid,
            "agentid": self.agent_id,
            "msgtype": "file",
            "file": {
                "media_id": media_id
            },
            "duplicate_check_interval": 600
        }).json()
        return r
