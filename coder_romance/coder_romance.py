# -*- coding: utf-8 -*-
import hashlib
import base64

ciphertext = 'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'
plaintext = ["我们在一起吧", "我选择原谅你", "别说话，吻我", "多喝热水"]

for i in plaintext:
    ha = hashlib.md5()
    ha.update(i.encode('utf-8'))
    ha_out = ha.hexdigest()
    jiami = base64.encodebytes(ha_out.encode('utf-8'))
    jiemi = jiami.decode('utf-8')
    if jiemi == ciphertext:
        print('你说了：' + i)
