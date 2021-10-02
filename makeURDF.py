import subprocess
subprocess.check_call("docker build -f Dockerfile.build . -t onshape-urdf-builder")
try:
    subprocess.check_call("docker container stop urdf-builder")
    subprocess.check_call("docker container rm urdf-builder")
except subprocess.CalledProcessError:
    pass
subprocess.check_call("docker run -t -d --name=urdf-builder onshape-urdf-builder")
subprocess.check_call("docker cp config.json urdf-builder:/root/catkin_ws/src/robot/model/config.json")
subprocess.check_call("docker exec urdf-builder bash -c \"cd /root/catkin_ws/src/robot && onshape-to-robot model\"")
subprocess.check_call("docker cp urdf-builder:/root/catkin_ws/src/robot/model output")
