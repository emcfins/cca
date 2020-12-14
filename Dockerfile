# Created by Erin to easily complile and run Fortran because my Mac wasn't having it
# Run command: docker run -it -v <project location>:/data 

FROM debian:8.6

RUN apt-get update -y && \
    apt-get install -y gcc \
		                   vim \
                       wget
RUN wget http://download2176.mediafire.com/t54rkghl5sdg/0gzrgdkk3bwzmfz/g77_all_debian_and_ubuntu.tar.gz && \
    tar xfvz g77_all_debian_and_ubuntu.tar.gz && \
    cd g77_all_debian_and_ubuntu && \
    if [[ `uname -m` = i*86 ]]; then dpkg -i *.i386.deb *all.deb; elif [[ `uname -m` = x*64 ]]; then dpkg -i *amd64.deb *all.deb; fi && \
    echo "LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LIBRARY_PATH" >> ~/.bashrc && \
    echo "export LIBRARY_PATH" >> ~/.bashrc && \
    ln -s /usr/lib/gcc/x86_64-linux-gnu/4.9/libgcc_s.so /usr/lib/x86_64-linux-gnu/

# Command to compile the file `g77 -o adventure.out advent.for`
CMD ["/bin/bash"]
