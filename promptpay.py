import libscrc
import qrcode

def get_payload(one_time_use, phone_number):
    payload = [
        '000201',
        f'0102{"12" if one_time_use else "11"}',
        '29370016A000000677010111',
        f'01130066{phone_number[1:]}',
        '5802TH',
        '5303764',
        '6304'
        ]
    
    payload = ''.join(payload)
    checksum = ('0000' + hex(libscrc.ccitt(payload.encode("ascii"), 0xFFFF))[2:])[-4:]
    payload += checksum

    return payload.upper()

one_time_use = True
phone_number = '0999999999'

payload = get_payload(one_time_use, phone_number)
print(payload)

promptpay_qr = qrcode.make(payload)
promptpay_qr.save('mypromptpay.png')