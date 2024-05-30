# pip install -q git+https://github.com/THU-MIG/yolov10.git
# yolov10n.pt ağırlık dosyasını çalışma klasörüne kopyala

from ultralytics import YOLOv10

model = YOLOv10('yolov10n.pt')

results = model(source='araba.jpg', conf=0.25, show=True)

print(results[0].boxes.xyxy)