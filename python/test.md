OpenStack Image acts as a registry for virtual disk images. Users can add new images or take a snapshot of an existing server for immediate storage. You can use the snapshots for backup or as templates for new servers. Registered images can be stored in the Object Storage service or in other locations, such as simple file systems or external Web servers.


The following image disk formats are supported: aki/ami/ari (Amazon kernel, ramdisk, or machine image) iso (archive format for optical discs, such as CDs) qcow2 (Qemu/KVM, supports Copy on Write) raw (unstructured format) vhd (Hyper-V, common for virtual machine monitors from vendors such as VMware, Xen, Microsoft, and VirtualBox) vdi (Qemu/VirtualBox) vmdk (VMware) Container formats can also be reg


OpenStack Orchestration advantages include: A single template provides access to all underlying service APIs. Templates are modular and resource-oriented. Templates can be recursively defined and reusable, such as nested stacks. The cloud infrastructure can then be defined and reused in a modular way. Resource implementation is pluggable, which allows for custom resources.

OpenStack Data Processing (sahara) OpenStack Data Processing enables the provisioning and management of Hadoop clusters on OpenStack. Hadoop stores and analyze large amounts of unstructured and structured data in clusters. Hadoop clusters are groups of servers that can act as storage servers running the Hadoop Distributed File System (HDFS), compute servers running Hadoop’s MapReduce (MR) framework, or both.



The servers in a Hadoop cluster need to reside in the same network, but they do not need to share memory or disks. Therefore, you can add or remove servers and clusters without affecting compatibility of the existing servers. The Hadoop compute and storage servers are co-located, which enables high-speed analysis of stored data. All tasks are divided across the servers and utilizes the local server resources.