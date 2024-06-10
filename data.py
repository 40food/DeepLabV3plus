#roboflow에서 데이터를 받는 코드

#pip install roboflow
#pip install -r requirements.txt

#데이터 다운로드

#재활용품 데이터
from roboflow import Roboflow
rf = Roboflow(api_key="Msv3FS46edHNlrLb9GYe")
project = rf.workspace("remate").project("remate")
version = project.version(2)
dataset = version.download("png-mask-semantic")

#차선 데이터
# from roboflow import Roboflow
# rf = Roboflow(api_key="Msv3FS46edHNlrLb9GYe")
# project = rf.workspace("automotive-lane-detection").project("lane-segment-rxqje")
# version = project.version(2)
# dataset = version.download("png-mask-semantic")
