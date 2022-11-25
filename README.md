# FastChat

## IMPLEMENTATION SO FAR:
1. Multi-client Multi-Server Connection
2. Login/ Sign Up Feature
3. Load Balancing of The Server
4. Storing of The Offline Messages
5. End to End Encrption Using pyCrpto
6. Random private key generation for each user using secrets module
7. Password and offline messages stored in database using hashlib
8. Input password with getpass module
9. Create groups, add & remove members from group (only admin) and send message to groups
10. Send images both offline and online

## TECH STACK:
1. python
2. mySQL
3. python socket library
4. hashlib
5. pycrpto
6. getpass
7. secrets
8. base64 encoding

## RUNNING INSTRUCTIONS
1. Start the server.py by running the python3 server.py file
2. Start client.py file by running python3 client.py file
3. Select if you want to sign-in or register
   - If you want to register, enter a unique name and your password
   - If you want to login, then enter your name and password
4. After login-in, Select whether you want to send a personal message, create a group, send message to an existing group, or log-out
5. After chosing the option, you will get an option to either send a message or send an image
6. Then you can type the message to send or insert image from directory4
7. If you select personal message then you will have to enter receiver's name
6. After each message you will the option to switch reciever, or switch to group chat or close the chat


## TEAM MEMBER'S CONTRIBUTION

1. AKSHAT SINGH (210020013)
   * MultiClient Connection
   * Load Balancer
   * Offline Messages
   * Performance Analysis
   * Group Creation

2. SHANTANU WELLING (210010076)
   * Encryption and Authentication
   * Offline Messages
   * Load Balancer
   * Performance Analysis
   * Group member addition and deletion

3. HARSHIT AGARWAL (210020054)
   * Image Transfer and Encryption
   * Offline Messages
   * Group Messages broadcasting
   * Sphinx Documentation













