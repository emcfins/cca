# Created by Erin to easily complile and run Fortran because my Mac wasn't having it
# Run command: docker run -it -v <project location>:/data 

#FROM debian:8.6
FROM debian:10.7

RUN apt-get update -y && \
    apt-get install -y gcc \
                       vim \
                       wget && \
    apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget http://gnxas.unicam.it/XASLABtars/g77_pack_64bit.tar && \
    tar xfv g77_pack_64bit.tar && \
    chmod +x ./install.sh && \
    sed -i 's/sudo //g' /install.sh && \
    ./install.sh && \
    echo "LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LIBRARY_PATH" >> ~/.bashrc && \
    echo "export LIBRARY_PATH" >> ~/.bashrc && \
#    ln -s /usr/lib/gcc/x86_64-linux-gnu/4.9/libgcc_s.so /usr/lib/x86_64-linux-gnu/
    ln -s /usr/lib/gcc/x86_64-linux-gnu/8/libgcc_s.so /usr/lib/x86_64-linux-gnu/

# Command to compile the file `g77 -o adventure.out advent.for`
CMD ["/bin/bash"]
