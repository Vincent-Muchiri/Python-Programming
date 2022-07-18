text = '10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 2222'

print(text.split()[3].strip("[]"))