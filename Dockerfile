RUN git clone -b main https://github.com/I-Himanshu/vcStreamBot

WORKDIR vcStreamBot

RUN pip3 install --no-cache-dir requirements.txt

CMD ["python3","runner.py"]
