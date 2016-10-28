# Created by Erin to easily complile and run Fortran because my Mac wasn't having it
# Run command: docker run -it -v <project location>:/data 

FROM debian:latest

RUN apt-get update && \
  apt-get install -y gcc gfortran

CMD ["/bin/bash"]
