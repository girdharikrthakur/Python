# Stack

print("========== Stack Data Structure ================")

# Stack
# is a LIF0 (Last In First Out)


browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)

print("rediract", browsing_session)


if not browsing_session:
    browsing_session[-1]
