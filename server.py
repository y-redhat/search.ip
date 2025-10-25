import socket
import threading

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1024

def handle_client(conn, addr):
    print(f"クライアント {addr} が接続しました。")
    
    with conn:
        try:
           
            data = conn.recv(BUFFER_SIZE)
            
            if data:

                message = data.decode('utf-8')
                
                print("\n--- 受信した情報 ---")
               
                print(f"OSが取得した接続元アドレス: {addr[0]}")
               
                print(f"メッセージデータ: {message}")
                print("---------------------\n")
                
               
                response_message = f"サーバー: 受信完了しました。メッセージ「{message[:40]}...」"
                conn.sendall(response_message.encode('utf-8'))
                
            else:
               
                print(f"クライアント {addr} からデータが送られてきませんでした。")

        except Exception as e:
            print(f"通信エラーが発生しました: {e}")
            
    print(f"クライアント {addr} との接続を閉じました。")


def start_server():
   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind((HOST, PORT))
        s.listen(5) 
        print(f"サーバーが {HOST}:{PORT} で待機中です...")
        
    
        while True:
           
            conn, addr = s.accept()
          
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()
