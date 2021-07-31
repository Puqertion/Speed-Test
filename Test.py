import speedtest

test = speedtest.Speedtest()

print("Loading Server List!")
test.get_servers()
print("Choosing Best Server!")
best = test.get_best_server()
print(f"Found : {best['host']} Located in {best['country']}")

print("Performing Download Test.")
download_result = test.download()
print("Performing Upload Test.")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download Speed : {download_result / 1024 / 1024:.2f} Mbit/s")
print(f"Upload Speed : {upload_result / 1024 / 1024:.2f} Mbit/s")
print(f"Ping : {ping_result:.2f} Ms")