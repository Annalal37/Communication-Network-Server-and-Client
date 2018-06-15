1.run server_TCP_modified.py

2.open windows command and cd to the file folder including TCP_Dos_client.py, run : python TCP_Dos_client.py http://localhost:9999/ 300

3.using apache to test TCP server:

cd to the file folder including ab.exe (In my computer, the path is E:\wamp64\bin\apache\apache2.4.27\bin);

run: ab -n 1000 -c 1 http://127.0.0.1:9999/ 		(the parameter in -n and -c can be changed arbitrarily)

see results in EE410 apache test server.docx 
(After increaseing the numbers of requests and number of mutiple requests to make at a time, we can see the number of
requests per second is decreasing to only 16.46 requests per second. So I limit the maximum thread number to protect server and 
then it can bear maximum 3000 requests per second when running ab -n 10000 -c 10000 http://127.0.0.1:9999/.)


For UDP server and client similarly:

4.run server_UDP_modified.py

5.open windows command and cd to the file folder including UDP_Dos_client.py, run : python TCP_Dos_client.py http://localhost:9999/ 300


