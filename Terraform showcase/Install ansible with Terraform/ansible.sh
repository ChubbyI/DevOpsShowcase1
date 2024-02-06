#!/bin/bash

sudo yum update -y
sudo yum install -y epel-release
sudo yum install -y ansible
sudo systemctl start ansible
sudo systemctl enable ansible
ansible --version
