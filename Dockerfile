# Created by Erin to easily complile and run Fortran because my Mac wasn't having it
# Run command: docker run -it -v <project location>:/data 

FROM debian:8.6

RUN apt-get update -y && \
    apt-get install -y gcc \
		                   vim \
                       wget
RUN wget http://gnxas.unicam.it/XASLABtars/g77_pack_64bit.tar && \
    tar xfv g77_pack_64bit.tar && \
    chmod +x ./install.sh && \
    sed -i 's/sudo //g' /install.sh && \
    ./install.sh

# Command to compile the file `g77 -o adventure.out advent.for`
CMD ["/bin/bash"]
