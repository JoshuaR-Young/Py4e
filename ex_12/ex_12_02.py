import socket

def get_host_path(url):
    try:
        if url.startswith('http://'):
            url = url[len('http://'):]
        elif url.startswith('https://'):
            url = url[len('https://'):]
        
        parts = url.split('/', 1)
        host = parts[0]
        path = '/' + parts[1] if len(parts) > 1 else '/'
        return host, path
    except Exception as e:
        print(f'Error parsing URL: {e}')
        return None, None

def main():
    url = input('Enter URL: ')
    host, path = get_host_path(url)
    
    if host is None or path is None:
        print('Invalid URL. Exiting.')
        return
    
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        
        cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
        mysock.send(cmd)
        
        total_chars = 0
        displayed_chars = 0
        limit = 3000
        
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            total_chars += len(data)
            if displayed_chars < limit:
                print(data.decode()[:limit-displayed_chars], end='')
                displayed_chars += len(data)
        
        mysock.close()
        print(f'\n\nTotal number of characters received: {total_chars}')
    except socket.gaierror:
        print('Failed to connect to host. Please check the URL and try again.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
