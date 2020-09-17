FROM python:3.8.0

RUN apt update \
	&& apt upgrade -y \
	&& pip install --upgrade pip 

# COPY ./predict.py $/home/cloudfonding-predict
# CMD ["python", "./predict.py"]

RUN pip install pandas \
	&& pip install numpy \
	&& pip install ipython \
	&& pip install scikit-learn \
	&& apt clean

WORKDIR /home/clouldfonding-predict

#docker run -it cloudfonding /bin/sh
