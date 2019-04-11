FROM docker.io/centos
RUN rm -f /etc/yum.repos.d/CentOS-Base.repo && \
    curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo && \
    yum clean all && \
    yum install -y make cmake epel-release  python-pip gcc gcc-c++ python-devel && \
    pip install face_recognition tornado==4.5 && \
    yum remove -y make cmake gcc gcc-c++
