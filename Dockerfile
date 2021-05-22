FROM python:3.9

WORKDIR /usr/src/app 

COPY requirement.txt ./

RUN python -m pip install -U pip
RUN python -m pip install pywin32==300

RUN pip install --no-cache-dir -r requirement.txt

COPY . .
RUN pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

CMD ["python3", "./price_tracker.py"]
