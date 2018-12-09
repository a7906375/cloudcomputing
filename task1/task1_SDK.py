#import docker
#client = docker.from_env()
#image = client.images.pull("nclcloudcomputing/javabenchmarkapp")
#container = client.containers.run("nclcloudcomputing/javabenchmarkapp", ports={'8080/tcp':83}, detach=True)

import docker
client = docker.from_env()
print client.containers.run("nclcloudcomputing/javabenchmarkapp",)
