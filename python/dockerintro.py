'''
CONTAINER:
        A container is an entity that has everything required to run your software. It packs:

Your software
All dependencies
All system tools and libraries that might be needed
Containers are like virtual machines but more lightweight. For instance, they start almost instantly. Containers virtualize just the operating system, while a VM virtualizes an entire machine with all its hardware.

'''

'''
Image: 
        A Docker container is always based on an image. You first define an image and then start one or more containers based on it. You can define an image in a file (called the Dockerfile) and this file can be checked into a VCS like git, together with your code. This allows you to document and create the exact environment needed to run your code.

You don’t have to build an image from scratch. Many software projects provide images that containerize their software. For practically all computer languages, including Python, there are multiple base images you can choose from.

Just like Python classespi, you can extend such images with your specifics, as I will demonstrate below. By doing so, you are adding a new layer on top of an existing image. Because of this layering, Docker images can be stored and built very efficiently. For example, many images might all share the same Debian Linux base image and extend it with their specific software requirements:
'''