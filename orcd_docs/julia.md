There are a number of versions of Julia that are currently available on our clusters (see here for information on using different modules). However, sometimes, you may need a specific version of Julia that is not provided. If this happens, you can download it. 

A complete list of previous Julia versions can be found here. From this site, copy the link to the tar.gz file that corresponds to the version you need. Be sure to select the version for a Linux operating system and x86_64 architecture.

Download the .tar file:
wget [link to file]


Extract the .tar file:
tar -xvzf [file name]


Add the downloaded version to your path:
export PATH="~/path/to/your/julia/directory/bin:$PATH"


The following example is for Julia 1.9.0:
wget https://julialang-s3.julialang.org/bin/linux/x64/1.9/julia-1.9.0-linux-x86_64.tar.gz
tar -xvzf julia-1.9.0-linux-x86_64.tar.gz
export PATH="~/julia-1.9.0/bin:$PATH"


