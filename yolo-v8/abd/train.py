import subprocess
command = f"yolo detect train model=yolov8n.pt data=data.yaml epochs=100"
subprocess.run(command, shell=True)