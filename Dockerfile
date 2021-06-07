FROM winamd64/python:3-windowsservercore

WORKDIR /usr/src/app 

COPY pywin32-300-cp39-cp39-win_amd64.whl .

RUN python -m pip install -U pip
RUN pip install pywin32-300-cp39-cp39-win_amd64.whl
#pywin32 not installing in docker.

COPY requirement.txt .
RUN pip3 install --no-cache-dir -r requirement.txt

COPY . .
RUN pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

CMD ["python3", "./price_tracker.py"]
