FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.4.2 pytest-testdox && npm i breathecode-cli@1.2.51 -g

