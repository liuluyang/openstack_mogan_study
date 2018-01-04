#coding:utf8

from hashlib import md5, sha1, sha224, sha256, sha384, sha512

hash_funcs = [md5, sha1, sha224, sha256, sha384, sha512]


def hash_show(s):
    result = []
    for func in hash_funcs:
        s_hash_obj = func(s)
        s_hash_hex = s_hash_obj.hexdigest()
        result.append((s_hash_obj.name, s_hash_hex,  len(s_hash_hex)))
    return result


if __name__ == '__main__':
    s = 'hello python'
    rs = hash_show(s)
    print(rs)