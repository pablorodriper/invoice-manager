FROM python:3.10

RUN apt update && yes | apt upgrade

# # Fix opencv
# RUN apt install ffmpeg libsm6 libxext6 -y

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create the user
ARG USERNAME=pablo
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME 

USER $USERNAME
ENTRYPOINT [ "/bin/bash" ]