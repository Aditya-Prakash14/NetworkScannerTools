import socket
import random
import string
import time

def generate_random_payload(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def fuzz_target(target_ip, target_port, num_requests, payload_length):
    for _ in range(num_requests):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((target_ip, target_port))
                payload = generate_random_payload(payload_length)
                print(f"Sending payload: {payload}")
                sock.sendall(payload.encode())
                time.sleep(0.5)  # Delay between requests
        except Exception as e:
            print(f"Error: {e}")

def main():
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    num_requests = int(input("Enter number of requests: "))
    payload_length = int(input("Enter payload length: "))
    
    fuzz_target(target_ip, target_port, num_requests, payload_length)

if __name__ == "__main__":
    main()
