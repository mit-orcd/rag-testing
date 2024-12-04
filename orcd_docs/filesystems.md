Large HPC systems often have different filesystems for different purposes. ORCD systems are no different, and each have their own approach. This page documents these.

Users each get a small home directory that is backed up and meant for important files. Larger scratch space is not backed up. Additional storage can be purchased. The Lustre scratch space will be faster than NFS for the majority of workloads, however having large numbers of small files will make it slower than NFS and can slow down the filesystem overall, so it is important to follow the Lustre Best Practices. See the Engaging Documentation Page on Storage for more information.

SuperCloud uses Lustre for all central/shared storage (accessible to all nodes in the system). This storage is not backed up. See the SuperCloud Best Practices and Performance Tips page for best practices using the Lustre filesystem. Quotas or limits are set on the storage as guardrails. Individual and group storage use and quotas can been viewed on the User Profile Page on the SuperCloud Web Portal (only accessible if you have an account). Additional storage may be granted on a case by case basis. Local disk spaces will be faster than the Lustre shared filesystem, but all are temporary and can only be accessed on the node where they are created.

OpenMind provides a number of different storage options. See the OpenMind Documentation page on Storage for more information, best practices, and recommendations.

