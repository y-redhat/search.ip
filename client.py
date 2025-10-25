import socket
import urllib.request 


HOST = '127.0.0.1'  
PORT = 65432        
BUFFER_SIZE = 1024  

def get_global_ip():

    
    try:
        url = 'http://checkip.amazonaws.com'
        with urllib.request.urlopen(url, timeout=5) as response:
            global_ip = response.read().decode('utf-8').strip()
       
        return global_ip
    except Exception as e:
       
        return "UNKNOWN_IP"


def start_client():
   
    
    
    fixed_message = "Hello Server! This is IP. hahaha"
    
    client_ip = get_global_ip()

    message = f"[IP:{client_ip}] {fixed_message}" 
    


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            
            s.connect((HOST, PORT))
           

            data_to_send = message.encode('utf-8')
            s.sendall(data_to_send)
           
            
            data_received = s.recv(BUFFER_SIZE)
            if data_received:
                response = data_received.decode('utf-8')
                print(f"サーバー応答: {response}")

                    
    print("See you、 good bye.")
