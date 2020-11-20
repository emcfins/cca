# Created by Erin to easily complile and run Fortran because my Mac wasn't having it
# Run command: docker run -it -v <project location>:/data 

FROM debian:8.6

RUN apt-get update -y && \
  apt-get install -y gcc \
                     gfortran \
		     vim 

CMD ["/bin/bash"]
