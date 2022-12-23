# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from python_on_whales import docker


mydock=docker.network.create("SE443_test", driver="overlay", subnet="10.10.10.0/24")
print(mydock.name)
print(mydock.id)
print(mydock.created)