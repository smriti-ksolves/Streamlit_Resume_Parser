FROM python:3.8-slim
ENV PYHTONUNBUFFERED=1
RUN apt-get update \
  && apt-get -y install tesseract-ocr\
  && apt-get -y install ffmpeg libsm6 libxext6
WORKDIR /usr/src/app
# Copy the requirements file
COPY requirements.txt .
# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application files
COPY . .

# Run the Flask application
CMD ["streamlit", "run", "streamlit_file.py"]