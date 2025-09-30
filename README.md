# Satellite Flood Pipeline

Pipeline thu thập ảnh vệ tinh từ **Google Earth Engine (GEE)** để phục vụ huấn luyện và kiểm thử mô hình dự báo lũ lụt.  
Dữ liệu được chia thành **train** và **test**, lưu dưới dạng **GeoTIFF** (`.tif`) kèm theo metadata (`.csv`).  

---

## Cài đặt

### 1. Clone repo
~~~
git clone https://github.com/<your-username>/satellite-flood-pipeline.git
cd satellite-flood-pipeline
~~~

### 2. Tạo virtualenv
~~~
python3 -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
~~~

### 3. Cài dependencies
~~~
pip install -r requirements.txt
~~~


## Kết nối Google Earth Engine
Cài đặt Earth Engine Python API.
Xác thực tài khoản:
~~~
 earthengine authenticate
~~~

## Sử dụng
~~~
python -m src.data.download_data_input
~~~
Script sẽ hỏi lần lượt mode, lat, lon, buffer, v.v.

## Output
Ảnh được lưu trong data/train/<region_name>/ hoặc data/test/<region_name>/
Mỗi ảnh có:
*_raw.tif → ảnh Sentinel gốc
*_preview.tif → ảnh RGB nén (0–255)
Metadata CSV gồm thông tin:
region_name, lat, lon
capture_date
cloud_percentage
bands
file_path_raw, file_path_preview
