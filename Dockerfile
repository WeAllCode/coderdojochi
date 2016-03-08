FROM python:2.7

MAINTAINER CoderDojoChi

ENV DIR_BUILD /build
ENV DIR_SRC /src

RUN mkdir -p $DIR_BUILD
RUN mkdir -p $DIR_SRC

WORKDIR $DIR_SRC

COPY requirements.txt $DIR_SRC/
RUN pip install -r requirements.txt

COPY manage.py $DIR_SRC/
COPY coderdojochi $DIR_SRC/coderdojochi
COPY fixtures /fixtures
COPY ./deploy.sh $DIR_BUILD/deploy.sh

CMD $DIR_BUILD/deploy.sh
