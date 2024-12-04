An SSH key is a secure access credential used in the SSH protocol and establishes a secure and encrypted connection to our HPC systems. This page is for those who wish to implement SSH key authentication on top of general MIT Kerberos authentication.

SSH keys consist of a pair: a public key and a private key. 

When you attempt to connect to an HPC system using SSH key authentication, the system uses your public key to initiate a challenge that can only be answered correctly using your private key. If the correct response is received, the system verifies your identity and grants access. 

Using the key and lock analogy, the private key is like your key, and the public key is like a lock you might place on a gym locker, which would be like your account on an ORCD system. You can leave the lock locked on the locker at the gym, because no one can open the lock without the key, but you wouldn't want to share your key with anyone else, because then they could get into your locker.

Do Not Share Your Private Key

Your private key should never be shared with anyone. If someone else obtains your private key, they could potentially gain unauthorized access to any system your key is associated with.

Before you generate an SSH key, you should check for existing SSH keys.  

If you do not have an existing SSH key, follow these steps. 

Save the key pair: You will be prompted to enter a file path to save the key. Press Enter to accept the default location:
Enter a file in which to save the key (/home/your_username/.ssh/id_rsa):


Passphrase: 
You will be asked to enter a passphrase for additional security. You can either enter a passphrase or leave it empty and press Enter:
Enter passphrase (empty for no passphrase):


Note

On ORCD systems, we recommend setting a passphrase as it provides extra security for your account by helping to prevent someone else from using your SSH keys. When you create a passphrase, your private key can only authenticate into your account when the correct passphrase is provided during login. Since you set your passphrase on your system, ORCD staff cannot help you remember or reset the passphrase for your SSH keys. You must create new SSH keys if you cannot remember your passphrase.

To upload your SSH key on our systems, you must update the authorized_keys file in the respective system via terminal. Alternatively, for the Engaging System, you have the option to use OnDemand, and for SuperCloud, you can fill out an SSH key addition form.

To add your SSH key via Terminal, please follow the steps outlined below:

Make sure to copy the entire line starting with ssh-rsa and ending with your email address or comment. 

Note

Do not remove anything already present in the authorized_keys file. Be careful to append your key to the end of the file rather than replacing its contents.

To add your SSH key to Engaging via OnDemand, please follow the steps outlined below:

Note

Do not remove anything already present in the authorized_keys file. Be careful to append your key to the end of the file rather than replacing its contents.

To add your SSH key to SuperCloud, please follow the steps outlined below:

To ensure that your SSH key is correctly configured, follow these steps:

If you encounter SSH key issues, you can reference the SSH Troubleshooting Checklist. While this guide is for SuperCloud, it should be helpful for other systems as well. If you are still having problems, please email us at orcd-help@mit.edu and visit the Getting Help page. In your help email, please include the output of the following command:
ssh -vvv USERNAME@cluster_address


