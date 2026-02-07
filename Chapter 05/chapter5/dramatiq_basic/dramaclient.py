from dramaserver import wait

# Fire-and-forget multiple messages
for i in range(10):
    wait.send(i, f"#{i}")

print("End Program")
