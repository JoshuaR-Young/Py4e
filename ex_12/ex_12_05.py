import socket

def get_url_data(url):
    try:
        #split URL to host and path
        parts = url.split('/', 3)
        if len(parts) < 3:
            raise ValueError('Invalid URL format')
        
        host = parts[2]
        path = '/' + parts[3] if len(parts) > 3 else '/'

        #create a socket connection
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
        mysock.send(cmd)

        received_data = b""
        headers_ended = False
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            received_data += data

            #check if we have received the end of the headers
            if not headers_ended:
                decoded_data = received_data.decode()
                header_end_index = decoded_data.find("\r\n\r\n")
                if header_end_index != -1:
                    headers_ended = True
                    #print data after the headers
                    print(decoded_data[header_end_index + 4:], end="")
            else:
                print(data.decode(), end="")

        mysock.close()
    except Exception as e:
        print(f"Error: {e}")

#prompt the user for the url
url = input('Enter URL: ')
get_url_data(url)
